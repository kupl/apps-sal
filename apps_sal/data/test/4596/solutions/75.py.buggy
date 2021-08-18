import numpy as np
n = int(input())
p = list(map(int, input().split()))
p = np.array(p)
cnt = 0
while cnt < 10000000:
    for i in p:
        if i % 2 != 0:
            print(cnt)
            return
    cnt += 1
    p = p // 2
