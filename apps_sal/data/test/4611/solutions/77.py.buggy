N = int(input())
t0, x0, y0 = 0, 0, 0
for i in range(N):
    t, x, y = list(map(int, input().split()))
    kyori = abs(x - x0) + abs(y - y0)
    time = abs(t0 - t)
    if abs(kyori - time) % 2 == 0 and time - kyori >= 0:
        t0, x0, y0 = t, x, y
    else:
        print('No')
        return
print('Yes')
