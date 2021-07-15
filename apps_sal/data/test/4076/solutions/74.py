import numpy as np
a,b,h,m = list(map(int,input().split()))

theta = abs(h/12-11*m/720)*2*np.pi
print(np.sqrt((a*a+b*b-2*a*b*np.cos(theta))))
