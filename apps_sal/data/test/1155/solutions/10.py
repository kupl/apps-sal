(n, m) = map(int, input().split())
ans = 10000000000.0
for i in range(n):
    (a, b) = map(int, input().split())
    ans = min(ans, a / b)
print(ans * m)
