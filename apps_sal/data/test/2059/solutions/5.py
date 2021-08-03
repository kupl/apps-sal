n = int(input())
a = list(map(int, input().split()))
ans = float('inf')
for i in range(n):
    ans = min(ans, a[i] // max(i, n - i - 1))
print(ans)
