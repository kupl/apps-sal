import math
a,b,h,m = list(map(int,input().split()))

minutes = m/60*2*math.pi
hour = (60*h+m)/720*2*math.pi

theta = abs(hour-minutes)


x = math.sqrt(a**2+b**2-2*a*b*math.cos(theta))
print(x)

