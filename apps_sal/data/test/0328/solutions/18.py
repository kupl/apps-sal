n = int(input())
ans = 0
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    ans = max(ans, x + y)
print(ans)
