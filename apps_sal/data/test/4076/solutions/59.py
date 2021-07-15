import numpy as np
a,b,h,m=map(int,input().split())
# print([a,b,h,m])

hour_theta= np.pi*(60*h+m)/360
minute_theta=np.pi*m/30

theta = abs(hour_theta-minute_theta)
# print(hour_theta)
# print(minute_theta)
# print(theta)
# print(np.cos(2.356194490192345))
ans=np.sqrt((a**2)+(b**2)-2*a*b*np.cos(theta))
print('{:.11f}'.format(ans))
