import numpy as np
n=int(input())
a=np.array([list(map(int,input().split())) for i in range(n)])
c=0
for i in a:
    for j in a:
        c+=np.linalg.norm(i-j)
print(c/n)
