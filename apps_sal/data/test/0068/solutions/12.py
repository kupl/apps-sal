def check(x, y, fx, fy, num_moves):
    if abs(fx - x) + abs(fy - y) - num_moves <= 0 and (abs(fx - x) + abs(fy - y) - num_moves) % 2 == 0:
        return True
    return False


N = int(input())
mm = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
dpmat = [[0] for i in range(4)]
ops = str(input())
for op in ops:
    dpmat[0].append(dpmat[0][-1])
    dpmat[1].append(dpmat[1][-1])
    dpmat[2].append(dpmat[2][-1])
    dpmat[3].append(dpmat[3][-1])
    dpmat[mm[op]][-1] = dpmat[mm[op]][-1] + 1
fpos = list(map(int, input().split()))
if N < fpos[0] + fpos[1]:
    print('-1')
else:
    (x, y) = (0, 0)
    ans = 100000000000.0
    while y <= N and x <= y:
        if y == 0 and x == 0:
            num_moves = 0
            xr = dpmat[3][N]
            xl = dpmat[2][N]
            yu = dpmat[0][N]
            yd = dpmat[1][N]
        else:
            num_moves = y - x + 1
            xr = dpmat[3][x - 1] + dpmat[3][N] - dpmat[3][y]
            xl = dpmat[2][x - 1] + dpmat[2][N] - dpmat[2][y]
            yu = dpmat[0][x - 1] + dpmat[0][N] - dpmat[0][y]
            yd = dpmat[1][x - 1] + dpmat[1][N] - dpmat[1][y]
        if check(xr - xl, yu - yd, fpos[0], fpos[1], num_moves) == True:
            x += 1
            ans = min(ans, num_moves)
        else:
            if x == 0:
                x += 1
            y += 1
    if ans == 100000000000.0:
        print('-1')
    else:
        print(max(0, ans))
