(b, g, n) = (int(input()), int(input()), int(input()))
badges = set()
for i in range(n + 1):
    if i <= b and n - i <= g:
        badges.add((i, n - i))
print(len(badges))
