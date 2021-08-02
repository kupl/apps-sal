mod = 10**9 + 7
n = int(input())
ans = pow(10, n, mod)
ans -= 2 * pow(9, n, mod)
ans += pow(8, n, mod)
ans %= mod
print(ans)
