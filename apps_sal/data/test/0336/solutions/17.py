# You lost the game.
n, a, b, c, d = list(map(int, input().split()))
r = 0
for e in range(1, n + 1):
    h = e + (a - d)
    i = h + (b - c)
    f = i + (d - a)
    if e == f + (c - b) and h <= n and i <= n and f <= n and h > 0 and i > 0 and f > 0:
        r += 1
print(r * n)
