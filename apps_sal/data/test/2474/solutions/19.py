n = int(input())
c = list(map(int, input().split()))
mod = 10**9+7
c.sort(reverse=True)
ans = 0
for k, num in enumerate(c):
    ans += (k+2)*num
    ans %= mod

for _ in range(2*n-2):
    ans *= 2
    ans %= mod

print(ans)
