n = int(input())
x = list(map(int, input().split()))
ans = 0
for i in range(1, n - 1):
    if x[i - 1] <= x[i] <= x[i + 1] or x[i + 1] <= x[i] <= x[i - 1]:
        ans += 1
print(ans)
