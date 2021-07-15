import sys
import math
a,b,h,m=map(int,input().split())

f=h / 12 * 360 - m / 60 * 360 + m / 60 / 12 * 360

print((a**2+b**2-2*b*a*(math.cos(math.radians(f))))**(0.5))
