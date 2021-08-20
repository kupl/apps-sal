from collections import deque


def bfs():
    q = deque()
    color1 = [-1] * (n + 1)
    color2 = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color1[i] == -1:
            color1[i] = i
            q.append(i)
            while q:
                p = q.popleft()
                for j in G[p]:
                    if color1[j] == -1:
                        color1[j] = color1[p]
                        q.append(j)
        if color2[i] == -1:
            color2[i] = i
            q.append(i)
            while q:
                p = q.popleft()
                for j in H[p]:
                    if color2[j] == -1:
                        color2[j] = color2[p]
                        q.append(j)
    group = [color1[i] + 200000 * color2[i] for i in range(n + 1)]
    return group


(n, k, l) = map(int, input().split())
G = [[] for _ in range(n + 1)]
H = [[] for _ in range(n + 1)]
for _ in range(k):
    (p, q) = map(int, input().split())
    G[p].append(q)
    G[q].append(p)
for _ in range(l):
    (r, s) = map(int, input().split())
    H[r].append(s)
    H[s].append(r)
group = bfs()
d = {}
for i in range(1, n + 1):
    if group[i] in d:
        d[group[i]] += 1
    else:
        d[group[i]] = 1
ans = [0] * n
for i in range(1, n + 1):
    ans[i - 1] = d[group[i]]
print(' '.join(map(str, ans)))
