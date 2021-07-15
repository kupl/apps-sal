from decimal import * 
a,b,x = list(map(int,input().split()))

ans = 0
d = 0

for i in range(10,0,-1):
    left = x - b*i
    if(left >= a*pow(10,i-1)):
        d = i
        break

    
if(d==0):
    print((0))
elif(d==10):
    print((10**9))
else:
    left = x - b*d
    left = Decimal(left) / Decimal(a)
    ans = int(left)
    if(ans>=pow(10,d)):
        ans = pow(10,d)-1
    print(ans)


    

