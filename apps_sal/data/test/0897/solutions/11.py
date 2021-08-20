MOD = 1000000007
(n, m) = map(int, input().split())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
probLeft = 1


def modInv(x, n=MOD - 2):
    if n <= 1:
        return x ** n % MOD
    tmp = modInv(x, n // 2) ** 2 % MOD
    if n % 2 == 1:
        tmp = tmp * x % MOD
    return tmp


dp = {}


def fraction(x, y):
    if (x, y) in dp:
        return dp[x, y]
    dp[x, y] = x * modInv(y) % MOD
    return dp[x, y]


minv = fraction(1, m)
ans = 0
for i in range(n):
    a = l1[i]
    b = l2[i]
    if a == 0 or b == 0:
        if b > 0:
            ans += probLeft * (m - b) * minv % MOD
        elif a > 0:
            ans += probLeft * (a - 1) * minv % MOD
        else:
            ans += probLeft * ((m - 1) * m // 2) * minv * minv % MOD
        probLeft = probLeft * minv % MOD
    elif a > b:
        ans += probLeft
        break
    elif a == b:
        continue
    else:
        break
print(ans % MOD)
