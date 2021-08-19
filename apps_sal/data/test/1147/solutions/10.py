from bisect import bisect_left


def R():
    return list(map(int, input().split()))


(n, x, k) = R()
a = sorted(R())
s = 0
for u in a:
    l = ((u - 1) // x + k) * x
    s += bisect_left(a, l + x) - bisect_left(a, max(u, l))
print(s)
