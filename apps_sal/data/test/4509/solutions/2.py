import math 
for i in range(int(input())):
    n,k=list(map(int,input().split()))
    e=math.ceil(k/(n-1))-1
    print(k+e)

