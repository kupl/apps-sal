import numpy as np

a,b,c,d = map(int,input().split())

x = np.array([a,b])
y = np.array([c,d])

m = np.outer(x, y)
ret = np.max(m)
print(ret)
