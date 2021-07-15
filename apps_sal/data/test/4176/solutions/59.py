import math
#h,w=map(int,input().split())
#S=[list(map(int,input().split())) for _ in range(h)]
a,b=list(map(int,input().split()))
print(((a*b)//math.gcd(a,b)))

