n = int(input())
ans = 0
for i in range(n):
    if 2 ** i <= n:
        ans = max(ans, 2 ** i)
print(ans)
