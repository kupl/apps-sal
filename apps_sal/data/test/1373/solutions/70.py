n, k = map(int, input().split())

p = 10**9+7
ans = 1
for i in range(k, n+1):
    ans += (i/2 * ((n-i+1+n) - (0+i-1))) + 1
    ans %= p
print(int(ans))
