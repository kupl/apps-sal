n = int(input())
x = y = k = 0
ans = 1
for i in range(n):
    a, b = map(int, input().split())
    if (x, y) == (a, b):
        continue
    ans += max(0, min(a, b) - max(x - 1, y - 1, k))
    k = min(a, b)
    x, y = a, b
print(ans)
