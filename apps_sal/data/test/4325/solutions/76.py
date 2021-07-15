import math
n,x,t = map(int,input().split())
ans = t*math.ceil(n/x)
print(ans)
