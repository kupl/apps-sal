import sys
s, n = 0, int(input())
t = list(map(int, sys.stdin.read().split()))
p = [(t[2 * i], t[2 * i + 1]) for i in range(n)]
for x, i in enumerate(p, 1):
    for j in p[x:]:
        a = b = 0
        for k in p:
            d = (i[0] - k[0]) * (j[1] - k[1]) - (i[1] - k[1]) * (j[0] - k[0])
            a, b = min(d, a), max(d, b)
        if a and b:
            s = max(s, b - a)
print(s / 2)
