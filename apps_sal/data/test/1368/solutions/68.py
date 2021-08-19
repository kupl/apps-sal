from itertools import accumulate


def comb(a, b):
    import math
    return math.factorial(a) // (math.factorial(a - b) * math.factorial(b))


(N, A, B) = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=1)
va = v[:A]
maxa = sum(va) / A
maxsum = sum(va)
print(maxa)
count = 1
if va[0] == va[-1]:
    v0 = va[0]
    v0c = v.count(v0)
    ans = comb(v0c, A)
    for i in range(A, B):
        if v[i] == v0:
            ans += comb(v0c, i + 1)
    print(ans)
else:
    v1 = va[-1]
    v1c = va.count(v1)
    v1c2 = v.count(v1)
    print(comb(v1c2, v1c))
