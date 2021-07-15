a,b,c,d=map(int,input().split())
c=(c*60+d)*0.5
d*=6
import math
ans=a**2+b**2-2*a*b*math.cos(math.radians(min(abs(d-c),360-(abs(d-c)))))
print(ans**0.5)
