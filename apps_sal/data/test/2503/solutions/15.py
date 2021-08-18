from numpy import array
n, k = map(int, input().split())

xy = []
F = [[0] * (2 * k + 1) for _ in range(2 * k + 1)]
for __ in range(n):
    x, y, c = input().split()
    x, y = int(x), int(y)
    if c == 'B':
        y += k
    x %= 2 * k
    y %= 2 * k

    for _ in range(2):
        x = (x + k) % (2 * k)
        y = (y + k) % (2 * k)
        F[y + 1][x + 1] += 1
        if x - k >= 0 and y - k >= 0:
            F[y + 1][x - k + 1] -= 1
            F[y - k + 1][x + 1] -= 1
            F[y - k + 1][x - k + 1] += 1
        elif y - k >= 0:
            F[y - k + 1][0] += 1
            F[y + 1][0] -= 1
            F[y - k + 1][x + 1] -= 1
            F[y - k + 1][x + k + 1] += 1
            F[y + 1][x + k + 1] -= 1
        elif x - k >= 0:
            F[0][x - k + 1] += 1
            F[0][x + 1] -= 1
            F[y + 1][x - k + 1] -= 1

            F[y + k + 1][x - k + 1] += 1
            F[y + k + 1][x + 1] -= 1
        else:
            F[0][x + 1] -= 1
            F[y + 1][0] -= 1
            F[0][0] += 1
            F[y + k + 1][0] += 1
            F[y + k + 1][x + 1] -= 1
            F[0][x + k + 1] += 1
            F[y + 1][x + k + 1] -= 1
            F[y + k + 1][x + k + 1] += 1
    if __ == 0:
        pass
ans = 0
m = 3

F = array(F)
for i in range(0, 2 * k):
    F[:, i + 1] += F[:, i]
for i in range(0, 2 * k):
    F[i + 1, :] += F[i, :]
print(F[:2 * k, :2 * k].max())
