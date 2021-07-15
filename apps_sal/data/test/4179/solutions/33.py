import numpy as np
n,m,c = list(map(int,input().split()))
b = list(map(int,input().split()))
b = np.array(b)
k = 0
for i in range(n):
    a = list(map(int,input().split()))
    a = np.array(a)
    ans = np.dot(a,b)
    if ans  +c > 0:
        k +=1
print(k)

