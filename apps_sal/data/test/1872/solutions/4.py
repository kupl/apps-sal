import math
n,r = list(map(int,input().split()))
a = math.pi/n
b = a/2
c = math.pi-a-b
side = r*math.sin(a)/(2*math.sin(c))
area = 0.5*math.sin(b)*side*r*n*4
print(area)

