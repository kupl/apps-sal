import math
a,b,c,d = list(map(int,input().split()))
a-=1
e = c*d//math.gcd(c,d)
print((b-b//c-b//d+b//e-(a-a//c-a//d+a//e)))

