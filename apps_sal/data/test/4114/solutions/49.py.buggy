N = int(input())

XYs = []
for _ in range(N):
    XYs.append(list(map(int, input().split())))

for i in range(101):
    for j in range(101):
        f = 1
        for k in range(N):
            if XYs[k][2] > 0:
                h = XYs[k][2] + abs(XYs[k][0] - i) + abs(XYs[k][1] - j)
                break
        for k in range(N):
            if max(h - abs(XYs[k][0] - i) - abs(XYs[k][1] - j), 0) != XYs[k][2]:
                f = 0
                break
        if f == 1:
            print(i, j, h)
            return
