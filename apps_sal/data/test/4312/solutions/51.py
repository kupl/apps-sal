import math
a,b,c,d=map(int,input().split())
if math.ceil(a/d)>=math.ceil(c/b):
    print("Yes")
else:
    print("No")
