from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def find_negative_loop(n, e):
    d = n * [10**20]
    d[0] = 0
    for h in range(n):
        for i, j, k in e:
            if d[j] > d[i] + k:
                d[j] = d[i] + k
                if h == n - 1:
                    return -1
    return max(-d[n - 1], 0)


def find_loop(n, e, flag):
    x = [0] * n
    d = deque()
    t = []
    c = 0
    for i in range(n):
        for j in e[i]:
            x[j] += 1
    for i in range(n):
        if x[i] == 0:
            d.append(i)
            t.append(i)
            c += 1
    while d:
        i = d.popleft()
        for j in e[i]:
            x[j] -= 1
            if x[j] == 0:
                d.append(j)
                t.append(j)
                c += 1
    if flag == 0:
        return c == n
    else:
        return t


def glaph_bfs(s, n, e):
    ans = [0] * n
    Q = [s]
    visited = {s}
    while Q:
        P = []
        for i in Q:
            ans[i] = 1
            for j in e[i]:
                if j in visited:
                    continue
                visited.add(j)
                P.append(j)
        Q = P
    return ans


n, m, p = map(int, input().split())
ef = [[]for _ in range(n)]
ee = [[]for _ in range(n)]
e = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    c -= p
    ef[a].append(b)
    ee[b].append(a)
    e.append((a, b, c))
eff = glaph_bfs(0, n, ef)
eef = glaph_bfs(n - 1, n, ee)
ee = []
for a, b, c in e:
    if eff[a] == 1 and eef[a] == 1 and eff[b] == 1 and eef[b] == 1:
        ee.append((a, b, -c))
print(find_negative_loop(n, ee))
