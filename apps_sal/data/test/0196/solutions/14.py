def pwr(a, n, m):
    if n == 0:
        return 1
    ans = pwr(a, n // 2, m)
    ans = ans * ans
    ans %= m
    if n % 2 == 1:
        return (ans * a) % m
    else:
        return ans


M = 1000000007
tx, tn = input().split()
x = int(tx)
n = int(tn)
ans = pwr(2, n + 1, M) * x
ans %= M
ans = ans - pwr(2, n, M) + 1
ans = (ans + M) % M
if x == 0:
    ans = 0
print(ans)
