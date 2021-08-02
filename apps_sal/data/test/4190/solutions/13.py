n = int(input())
a = map(int, input().split())
d = [0] * n
for v in map(int, input().split()):
    d[v] += 1
p = list(range(1, n)) + [0]
r = []
for x in a:
    v = (n - x) % n
    while d[v] == 0:
        if d[p[v]] == 0:
            p[v] = p[p[v]]
        v = p[v]
    r += [(x + v) % n]
    d[v] -= 1
for i in r:
    print(i, end=" ")
