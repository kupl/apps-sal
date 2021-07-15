import math

p,r = list(map(int,input().split() ))

print((math.sin(math.pi/p)**2 /math.tan(1.5*math.pi/p) - math.sin(2*math.pi/p)/2)*-r*r*p)

