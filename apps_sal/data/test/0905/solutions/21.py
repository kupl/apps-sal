n, s = map(int, input().split())
ans = -1
for i in range(n):
    x, y = map(int, input().split())
    if y == 0 and x <= s or y != 0 and x < s:
        ans = max(ans, (100 - y) % 100)
print(ans)
