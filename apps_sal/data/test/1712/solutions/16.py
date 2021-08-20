(n, x, y) = [int(x) for x in input().split()]
dp = []
(cx, cy) = (0, 0)
while cx < x and cy < y:
    if (cx + 1) / x > (cy + 1) / y:
        dp.append('Vova')
        cy += 1
    elif (cx + 1) / x < (cy + 1) / y:
        dp.append('Vanya')
        cx += 1
    else:
        dp.append('Both')
        dp.append('Both')
        cx += 1
        cy += 1
for i in range(n):
    print(dp[(int(input()) - 1) % (x + y)])
