import numpy as np
a,b,h,m = list(map(int,input().split()))
pos1 = [b*np.sin(np.radians(6*m)),b*np.cos(np.radians(6*m))]
pos2 = [a*np.sin(np.radians(30*h+m*(360/(12*60)))),a*np.cos((np.radians(30*h+m*(360/(12*60)))))]
d = ((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)**0.5
print(d)
#print(pos1)
#print(pos2)

