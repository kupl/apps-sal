import math
a,b,c = list(map(int,input().split()))
v1 = (math.sqrt(2)*a**3)/12
v2 = b**3/(3*math.sqrt(2))
x = c/(2*math.cos(0.9424777960769379717))
v3 = (5*c**2*math.tan(0.9424777960769379717)*math.sqrt(c**2-x**2))/12
print(v1+v2+v3)

