import numpy as np
n = int(input())
p = list(map(int, input().split()))
p = p - np.ones((n,))
swapped = np.zeros((n - 1,))
now = 0
noc = 1

for now in range(0, n - 1):
    for i in range(now, n):
        if (p[i] == now):
            if(p[i] < i):
                for j in range(int(i - 1), int(p[i] - 1), -1):
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
