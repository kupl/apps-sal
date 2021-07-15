n, k, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
a.sort()
ans = 0
sm = sum(a)
ans = 0
for i in range(min(n, m // sm) + 1):
    ansn = (k + 1) * i
    tm = m - i * sm
    for j in range(k):
        q = min(n - i, max(0, tm // a[j]))
        ansn += q
        tm -= q * a[j]
    ans = max(ansn, ans)
print(ans)
