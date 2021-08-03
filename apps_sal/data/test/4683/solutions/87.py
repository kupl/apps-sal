n = int(input())
a = list(map(int, input().split()))
a_sum = sum(a)
ans = 0
mod = 10**9 + 7

for i in range(n - 1):
    a_sum = a_sum - a[i]
    ans += a[i] * a_sum

print(ans % mod)
