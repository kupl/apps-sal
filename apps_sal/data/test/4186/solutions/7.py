n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n // 2):
    ans += a[2 * i] - a[2 * i + 1]
print(-ans)
