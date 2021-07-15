import numpy as np
pr = np.ones(10**6+1)
pr[0] = pr[1] = 0
for k in range(4, 10**6+1, 2):
    pr[k] = 0
for i in range(3,10**3,2):
    if pr[i] == 1:
        for k in range(i*2, 10**6+1, i):
            pr[k] = 0
x = int(input())
while(True):
    if pr[x] == 1:
        print(x)
        return
    x += 1
