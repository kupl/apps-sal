import numpy as np
N = int(input())
AB = np.vstack([list(map(int, input().split())) for _ in range(N)])
meds = np.median(AB, axis=0)
if N % 2 == 0:
    print(int((meds[1] - meds[0]) * 2 + 1))
else:
    print(int(meds[1] - meds[0] + 1))
