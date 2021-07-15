N = int(input())
T = []
XY = []


def f(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


cx, cy = 0, 0
ct = 0
for _ in range(N):
    t, x, y = list(map(int, input().split()))
    d = f(cx, cy, x, y)
    # print(f'{ct=}, {t=}, {d=}')
    if d > t - ct:
        print('No')
        return
    if (t - ct - d) % 2 != 0:
        print('No')
        return
    cx, cy = x, y
    ct = t
print('Yes')

