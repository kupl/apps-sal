import math
a,b,h,m=list(map(int,input().split()))

arg=min(abs(30*h-5.5*m), 360-abs(30*h-5.5*m))

print((math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(arg)))))

