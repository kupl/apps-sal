n = int(input())
XYH = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[2])

for x in range(101):
    for y in range(101):
        hmax = XYH[0][2] + abs(x-XYH[0][0]) + abs(y-XYH[0][1])
        for i in range(n):
            if max(hmax-abs(x-XYH[i][0])-abs(y-XYH[i][1]), 0) != XYH[i][2]:
                break
            if i==n-1:
                print(x, y, hmax)
                return
