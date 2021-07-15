import numpy as np

w, h, n = list(map(int, input().split()))
area = np.zeros((w, h))

for i in range(n):
    x, y, a = list(map(int, input().split()))
    if a==1:
        area[:x, :] = 1
    elif a==2:
        area[x:, :] = 1
    elif a==3:
        area[:, :y] = 1
    else:
        area[:, y:] = 1

print(((w*h) - int(area.sum())))

