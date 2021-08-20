n = int(input())
a = [input() for _ in [0] * n]
ans = 0
for y in range(1, n - 1):
    for x in range(1, n - 1):
        if a[y][x] == a[y - 1][x - 1] == a[y - 1][x + 1] == a[y + 1][x - 1] == a[y + 1][x + 1] == 'X':
            ans += 1
print(ans)
