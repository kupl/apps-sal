import numpy as np
N = int(input())

cnt = np.zeros((10,10))

for x in map(str,range(0,N+1)):
    cnt[int(x[0]),int(x[-1])] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        ans += cnt[i,j] * cnt[j,i]

print(int(ans))
