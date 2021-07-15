n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = 0
    for j in range(n - i):
        x ^= a[i + j]
        ans = max(ans, x)
print(ans)
