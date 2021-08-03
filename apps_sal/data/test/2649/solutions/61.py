import numpy as np

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

xy45 = [[xy[i][0] - xy[i][1], xy[i][0] + xy[i][1]] for i in range(N)]
xy45 = np.array(xy45)

print((max(max(xy45[:, 0]) - min(xy45[:, 0]), max(xy45[:, 1]) - min(xy45[:, 1]))))
