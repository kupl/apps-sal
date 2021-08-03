x = []
y = []
all = []
for i in range(8):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)
    all.append((xx, yy))
sx = set(x)
sy = set(y)
if len(sx) % 3 != 0 or len(sy) % 3 != 0:
    print('ugly')
else:
    sx = sorted(list(sx))
    sy = sorted(list(sy))
    # print(sx)
    # print(sy)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if not (sx[i], sy[j]) in all:
                print('ugly')
                return
    print('respectable')
