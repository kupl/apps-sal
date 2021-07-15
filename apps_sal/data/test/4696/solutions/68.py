import numpy as np
s=list(map(int,input().split()))

p=np.prod(s)
if(p%2==0):
    print('Even')
else:
    print('Odd')
