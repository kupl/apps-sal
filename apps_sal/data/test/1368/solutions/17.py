from math import factorial as f


def comb(n, k):
    return f(n) // f(k) // f(n - k)


n, a, b = map(int, input().split())
V = sorted(map(int, input().split()))
s = sum(V[-a:]) / a
print(s)
small = V[-a]
cnt = V[-a:].count(small)
total = V.count(small)
if V[-1] != small:
    ans = comb(total, cnt)
else:
    ans = 0
    for i in range(a, min(b, total) + 1):
        ans += comb(total, i)
print(ans)
