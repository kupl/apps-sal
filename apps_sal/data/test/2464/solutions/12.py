import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**5)
def I(): return list(map(int, input().split()))


n, = I()
r = [[1 for i in range(n)], [1 for i in range(n)]]
p = [[i for i in range(n)], [i for i in range(n)]]


def find(x, c):
    if x != p[c][x]:
        p[c][x] = find(p[c][x], c)
    return p[c][x]


def union(a, b, c):
    x = find(a, c)
    y = find(b, c)
    mm = min(x, y)
    if x != y:
        p[c][y] = p[c][x] = mm
        r[c][mm] += r[c][max(x, y)]


an = 0
for i in range(n - 1):
    a, b, c = I()
    union(a - 1, b - 1, c)
vis = [0] * n
cc = []
for i in range(n):
    s0 = r[0][i]
    s1 = r[1][i]
    if p[0][i] == i:
        an += (s0 - 1) * s0
    if p[1][i] == i:
        an += (s1 - 1) * s1
    an += (r[1][find(i, 1)] - 1) * (r[0][find(i, 0)] - 1)
print(an)
