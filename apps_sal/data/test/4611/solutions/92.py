N = int(input())
pt, px, py = 0, 0, 0
can = True
for i in range(N):
    t, x, y = map(int, input().split())
    T, X, Y = t - pt, abs(x - px), abs(y - py)
    if T < X + Y or T % 2 != (X + Y) % 2:
        can = False
    pt, px, py = t, x, y
print('Yes' if can else 'No')
