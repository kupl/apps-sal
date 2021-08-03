w, h, n = list(map(int, input().split()))

sx = [0, w]
sy = [0, h]

for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        sx[0] = max(sx[0], x)
    if a == 2:
        sx[1] = min(sx[1], x)
    if a == 3:
        sy[0] = max(sy[0], y)
    if a == 4:
        sy[1] = min(sy[1], y)

print((max(0, max(0, (sx[1] - sx[0])) * max(0, (sy[1] - sy[0])))))
