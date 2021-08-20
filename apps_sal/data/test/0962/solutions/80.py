import sys
sys.setrecursionlimit(10 ** 6)
(n, m) = list(map(int, input().split()))
e = [[] for _ in range(n)]
for _ in range(m):
    (a, b) = list(map(int, input().split()))
    e[a - 1].append(b - 1)
c = [0] * n
ans = []


def search_path(p, temp):
    c[p] = 1
    for x in e[p]:
        if x in temp:
            print(-99999)
            return
        else:
            search_path(x, temp + [x])


t = 1
for i in range(n):
    if c[i] == 0:
        ans = search_path(i, [i])
print(-1)
