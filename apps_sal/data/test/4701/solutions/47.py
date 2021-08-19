n = int(input())
k = int(input())
ans = 1
for i in range(0, n):
    ans = min(2 * ans, ans + k)
print(ans)
