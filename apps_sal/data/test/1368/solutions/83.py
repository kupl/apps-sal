from collections import Counter
from math import factorial


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


(n, a, b) = list(map(int, input().split()))
v = list(map(int, input().split()))
v.sort(reverse=True)
cnt = Counter(v)
print(sum(v[:a]) / a)
if v[0] == v[a - 1]:
    x = cnt[v[0]]
    ans = 0
    for i in range(a, min(x, b) + 1):
        ans += comb(x, i)
    print(ans)
else:
    x = cnt[v[a - 1]]
    for i in range(a):
        if v[i] == v[a - 1]:
            y = i
            break
    print(comb(x, a - y))
