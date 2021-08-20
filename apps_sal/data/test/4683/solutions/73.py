n = int(input())
a = list(map(int, input().split()))
mod = 1000000007
sum = 0
ans = 0
for i in range(n):
    ans = (ans + a[i] * sum) % mod
    sum += a[i]
print(ans)
