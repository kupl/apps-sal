n, m = map(int, input().split())
ans = float('inf')
for x in range(n):
    a, b = map(int, input().split())
    ans = min(ans, m * (a / b))
print(ans)
