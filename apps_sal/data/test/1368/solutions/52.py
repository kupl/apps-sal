from collections import Counter


def comb(n, r):
    if n < r:
        return 0
    comb = 1
    r = min(r, n - r)
    for i in range(r):
        comb = comb * (n - i) // (i + 1)
    return comb


n, a, b = map(int, input().split())
v = list(map(int, input().split()))

v.sort(reverse=True)

va_count = Counter(v[:a])
v_count = Counter(v)

print(sum(v[:a]) / a)

if v[0] == v[a - 1]:
    print(sum(comb(v_count[v[0]], i) for i in range(a, b + 1)))
else:
    print(comb(v_count[v[a - 1]], va_count[v[a - 1]]))
