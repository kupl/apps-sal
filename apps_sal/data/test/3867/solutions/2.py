from collections import deque


def removeUsed(adj, used):
    to_remove = []
    for s in adj:
        if used[s]:
            to_remove.append(s)
    for s in to_remove:
        adj.remove(s)


def solve(a, s):
    if s[0] != 0:
        return False
    q = deque()
    q.append(0)
    i, n, cur = 1, len(a), -1
    used = [False] * n
    used[0] = True
    while i < n:
        if cur == -1:
            cur = q.popleft()
            removeUsed(a[cur], used)
        if not a[cur]:
            cur = -1
            continue
        cur_s = s[i]
        i += 1
        if cur_s not in a[cur]:
            return False
        a[cur].remove(cur_s)
        q.append(cur_s)
        used[cur_s] = True
    return True


n = int(input())
a = [set() for i in range(n)]
for i in range(n - 1):
    u, v = list(map(int, input().split()))
    a[u - 1].add(v - 1)
    a[v - 1].add(u - 1)
s = [(x - 1) for x in map(int, input().split())]
print("Yes" if solve(a, s) else "No")
