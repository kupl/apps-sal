(n, l, ans, p) = (int(input()), [*map(int, input().split())], 0, 0)
for i in range(n - 1, -1, -1):
    p += l[i] // 2
    if l[i] % 2 & (p > 0):
        ans += 1
        p -= 1
print(ans + 2 * p // 3)
