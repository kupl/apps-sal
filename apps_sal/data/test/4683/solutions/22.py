n = int(input())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7
ans = 0
total = sum(a)
for i in range(n):
    total -= a[i]
    ans = (ans + total * a[i]) % mod

print(ans)
