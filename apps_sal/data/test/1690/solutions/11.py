n = int(input())
a = list(map(int, input().split()))
r = 10 ** 10
ans = 0
for i in range(n):
    r = max(min(r - 1, a[n - i - 1]), 0)
    ans += r
print(ans)
