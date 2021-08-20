(n, m) = map(int, input().split())
ans = 0
for i in range(n):
    ans = max(ans, min(map(int, input().split())))
print(ans)
