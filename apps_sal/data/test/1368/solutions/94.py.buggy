from scipy.special import comb
ans = 0
N, A, B = map(int, input().split())
L = list(map(int, input().split()))
# Aこの平均でよい
L = sorted(L, reverse=True)
if len(set(L)) == 1:
    print(L[0])
    for i in range(A, B + 1):
        ans += comb(N, i, exact=True)
    print(ans)
    return
print(sum(L[:A]) / A)
R = list(L[:A])
c = L[A - 1]
if len(set(R)) == 1:
    n = L.count(c)
    for i in range(A, min(n, B) + 1):
        ans += comb(n, i, exact=True)
    print(ans)
    return
a = L.count(c)
b = R.count(c)
print(comb(a, b, exact=True))
