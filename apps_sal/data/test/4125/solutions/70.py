import numpy as np
n,X = map(int,input().split())
x = list(map(int,input().split()))
x.append(X)
x = sorted(x)
dis = []
for i in range(n):
  dis.append(x[i+1]-x[i])
print(np.gcd.reduce(dis))
