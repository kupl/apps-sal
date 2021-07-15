mod = 10 ** 9 + 7

N = int(input())
C = list(map(int, input().split()))
C.sort(reverse=True)

if N == 1:
    print(2 * C[0] % mod)
    return

ans = 0
coef = pow(2, N-1, mod)
for c in C:
    ans += c * coef
    ans %= mod
    coef = (coef + pow(2, N - 2, mod)) % mod

ans *= pow(2, N, mod)
ans %= mod
print(ans)
