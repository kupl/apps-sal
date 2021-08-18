import numpy as np
n = int(input())
p = list(map(int, input().split()))
swapped = np.zeros((n - 1,))
now = 0
noc = 1

for now in range(0, n - 1):
    for i in range(now, n):
        if (p[i] - 1 == now):
            if(p[i] - 1 < i):
                for j in range(i - 1, p[i] - 2, -1):
                    if swapped[j] != 0:
                        print(-1)
                        return
                    kari = p[j]
                    p[j] = p[j + 1]
                    p[j + 1] = kari
                    swapped[j] = noc
                    noc += 1
            break
for i in range(0, n - 1):
    if int(swapped[i]) == 0:
        print(-1)
        return
for i in range(0, n - 1):
    print(int(swapped[i]))
