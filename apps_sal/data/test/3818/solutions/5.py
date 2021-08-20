from collections import deque, defaultdict


def diameter(n, links):
    q = deque([0])
    stacked = {0}
    v = -1
    while q:
        v = q.popleft()
        for u in links[v]:
            if u not in stacked:
                q.append(u)
                stacked.add(u)
    v1 = v
    q = deque([(0, v1)])
    distances1 = [-1] * n
    distances1[v1] = 0
    while q:
        (d, v) = q.popleft()
        for u in links[v]:
            if distances1[u] == -1:
                q.append((d + 1, u))
                distances1[u] = d + 1
    v2 = v
    q = deque([(0, v2)])
    distances2 = [-1] * n
    distances2[v2] = 0
    while q:
        (d, v) = q.popleft()
        for u in links[v]:
            if distances2[u] == -1:
                q.append((d + 1, u))
                distances2[u] = d + 1
    return (v1, v2, distances1, distances2)


def solve(n, links):
    MOD = 10 ** 9 + 7
    (v1, v2, distances1, distances2) = diameter(n, links)
    ans = distances1[v2] * pow(2, n - 2, MOD) % MOD
    farther = defaultdict(lambda: [0, 0])
    for i in range(n):
        if i == v1 or i == v2:
            continue
        d1 = distances1[i]
        d2 = distances2[i]
        mx = max(d1, d2)
        mn = min(d1, d2)
        farther[mx][0] += 1
        farther[mx][1] = max(farther[mx][1], mn)
    m = n - 2
    max_smaller_d = 0
    for d in sorted(list(farther.keys()), reverse=True):
        if d <= max_smaller_d:
            ans = (ans + max_smaller_d * pow(2, m, MOD)) % MOD
            break
        (cnt, mn) = farther[d]
        m -= cnt
        ans = (ans + d * (pow(2, cnt, MOD) - 1) * pow(2, m, MOD)) % MOD
        max_smaller_d = max(max_smaller_d, mn)
    else:
        ans = (ans + max_smaller_d * pow(2, m, MOD)) % MOD
    return ans * 2 % MOD


n = int(input())
links = [set() for _ in range(n)]
for _ in range(n - 1):
    (a, b) = list(map(int, input().split()))
    a -= 1
    b -= 1
    links[a].add(b)
    links[b].add(a)
print(solve(n, links))
