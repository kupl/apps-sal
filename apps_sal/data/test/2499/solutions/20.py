def get_basis(a):
    basis = []
    for e in a:
        for b in basis:
            e = min(e, e ^ b)
        if e:
            basis.append(e)
    return basis


n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    ans ^= i
k = ~ans
for i in range(n):
    a[i] &= k
rank = 0
basis = get_basis(a)
res = 0
for i in basis:
    res = max(res, res ^ i)
print(ans + 2 * res)
