import sys
c, n = 0, int(input())
t = list(map(int, sys.stdin.read().split()))
p = [complex(t[i], t[i + 1]) for i in range(0, 2 * n, 2)]
for x, i in enumerate(p, 1):
    for j in p[x:]:
        a = b = 0
        for k in p:
            if k == i or k == j:
                continue
            d = (i.real - k.real) * (j.imag - k.imag) - (i.imag - k.imag) * (j.real - k.real)
            a, b = min(d, a), max(d, b)
        if a and b:
            c = max(c, b - a)
print(c / 2)
