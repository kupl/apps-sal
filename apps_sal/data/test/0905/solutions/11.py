(n, s) = list(map(int, input().split()))
ans = -1
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if x == s and y == 0:
        ans = max(ans, 0)
    if x < s:
        ans = max(ans, (100 - y) % 100)
print(ans)
