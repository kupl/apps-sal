import numpy as np
n=int(input())
x=1
for i in range(2,n+1):
    x=np.lcm(x,i)#今までの最小公倍数との最小公倍数を求める
print(x+1)
