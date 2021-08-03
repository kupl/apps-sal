x0, y0, ax, ay, bx, by = map(int, input().split())

x, y, t = map(int, input().split())

s = [x, y]

a = []

cnt = 70

for i in range(cnt):
    a.append([x0, y0])
    x0 = ax * x0 + bx
    y0 = ay * y0 + by

ans = 0


def dist(a1, b):
    return abs(a1[0] - b[0]) + abs(a1[1] - b[1])


for i in range(cnt):
    for j in range(i + 1):
        for k in range(i, cnt):
            if dist(s, a[i]) + dist(a[i], a[j]) + dist(a[j], a[k]) <= t:
                ans = max(ans, k - j + 1)
            if dist(s, a[i]) + dist(a[i], a[k]) + dist(a[k], a[j]) <= t:
                ans = max(ans, k - j + 1)

print(ans)
