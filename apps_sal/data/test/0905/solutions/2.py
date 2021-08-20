(n, s) = map(int, input().split())
mx = -1
for i in range(n):
    (xi, yi) = map(int, input().split())
    if xi <= s:
        if xi < s:
            mx = max(mx, (100 - yi) % 100)
        elif yi == 0:
            mx = max(0, mx)
print(mx)
