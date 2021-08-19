(n, d) = list(map(int, input().split()))
ans = 0
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if (x ** 2 + y ** 2) ** 0.5 <= d:
        ans += 1
print(ans)
