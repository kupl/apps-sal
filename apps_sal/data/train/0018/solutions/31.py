import math 
r=math.pi
for _ in range(int(input())):
    N=int(input())
    w=2*N
    t=(math.cos(r/w))/(math.sin(r/w))
    print(t)
