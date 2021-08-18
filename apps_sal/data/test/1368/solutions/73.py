from functools import lru_cache


@lru_cache
def comb(n, k):
    if k == 0:
        return 1
    elif n == k:
        return 1
    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)


N, A, B = map(int, input().split())
vs = sorted(map(int, input().split()), reverse=True)

print(sum(vs[:A]) / A)
v_replaceable = vs[A]

n = vs.count(v_replaceable)
a = A - vs.index(v_replaceable)
b = min(n, B - vs.index(v_replaceable))

if vs[0] == v_replaceable:
    print(sum(comb(n, t) for t in range(a, b + 1)))
else:
    print(comb(n, a))
