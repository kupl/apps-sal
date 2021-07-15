n, c = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 0
for i in range(len(x) - 1):
    ans = max(ans, x[i] - x[i + 1] - c)
print(ans)

