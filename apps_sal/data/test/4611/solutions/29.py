import numpy as np
N = int(input())

txy = [[0,0,0]]
for i in range(N):
    txy.append(list(map(int,input().split())))

out='Yes'
for i in range(1,N+1):
    x = np.array(txy[i])
    y = np.array(txy[i-1])
    mv = abs(x-y)
    # print(mv)
    dam = mv[0] - (mv[1] + mv[2])
    if dam%2==1 or dam<0:
        out='No'

print(out)

