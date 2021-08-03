import numpy as np

N = int(input())
arr = np.array(list(map(int, input().split())))
cnt = 0
while True:
    if np.sum(arr % 2) > 0:
        break
    else:
        arr = arr / 2
        cnt += 1
print(cnt)
