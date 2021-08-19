(n, m) = list(map(int, input().split()))
ans = 10 ** 40
for _ in range(n):
    (a, b) = list(map(int, input().split()))
    ans = min(ans, a / b * m)
print(ans)
