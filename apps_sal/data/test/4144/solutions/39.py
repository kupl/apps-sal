mod = 10**9 + 7
N = int(input())
ans = pow(10,N,mod)
ans -= 2 * pow(9,N,mod)
ans += pow(8,N,mod)
ans %= mod

print(ans)
