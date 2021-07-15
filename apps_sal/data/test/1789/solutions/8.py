a,b,x,y = map(int,input().split())
d = abs(2*b+1-2*a)
Yd = min([2*x,y])
print(d//2*Yd+x)
