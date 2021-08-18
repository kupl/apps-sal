from math import atan2, pi

N = int(input())
engines = []
total_X = total_Y = 0
for i in range(N):
    x, y = map(int, input().split())
    engines.append((atan2(y, x), x, y))
    total_X += x
    total_Y += y

engines.sort()
ans2 = 0
l = r = 0
X = engines[0][1]
Y = engines[0][2]

for l in range(N):
    theta = engines[l][0]
    xl, yl = engines[l][1:]
    while r + 1 - l < N \
        and (theta <= engines[(r + 1) % N][0] < theta + pi or
             theta <= engines[(r + 1) % N][0] + 2 * pi < theta + pi):
        r += 1
        X += engines[r % N][1]
        Y += engines[r % N][2]
    ans2 = max(ans2, X**2 + Y**2, (total_X - X)**2 + (total_Y - Y)**2)
    while r + 1 - l < N \
        and (theta <= engines[(r + 1) % N][0] <= theta + pi or
             theta <= engines[(r + 1) % N][0] + 2 * pi <= theta + pi):
        r += 1
        X += engines[r % N][1]
        Y += engines[r % N][2]
    ans2 = max(ans2, X**2 + Y**2, (total_X - X)**2 + (total_Y - Y)**2)
    X -= xl
    Y -= yl

print(ans2 ** 0.5)
