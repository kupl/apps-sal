import math
k,n,s,p=list(map(int,input().split()))
print(int(math.ceil(k*math.ceil(n/s) /p)    ))

