n, k = map(int, input().split())
g = n * 2 // ((k + 1) * k)
if not g:
    print(-1)
    return
ee = [2 ** i for i in range(31) if not n % 2 ** i]
x = n // ee[-1]
oo = [(o, x // o) for o in range(1, int(x ** .5) + 1, 2) if not x % o]
g = max(o * e for t in oo for o in t for e in ee if o * e <= g)
print(' '.join(map(str, range(g, g * k, g))), n - g * (k - 1) * k // 2)
