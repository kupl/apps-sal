mod = 10**9 + 7


def pow(num, p):
    nonlocal mod
    if p == 1:
        return num
    ans = pow(num, p // 2)
    if p % 2 == 0:
        return ans * ans % mod
    else:
        return ans * ans * num % mod


A, B, n, x = tuple(map(int, input().split()))

if A != 1:
    ans = B
    ans *= ((pow(A, n) - 1) % mod * (pow(A - 1, mod - 2) % mod)) % mod
    ans += pow(A, n) * x % mod
    ans %= mod
else:
    ans = x + n * B
    ans %= mod


print(round(ans))
