(n, s) = list(map(int, input().split()))
ans = -1
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if 100 * x + y > 100 * s:
        continue
    ans = max(ans, 0 if y == 0 else 100 - y)
print(ans)
