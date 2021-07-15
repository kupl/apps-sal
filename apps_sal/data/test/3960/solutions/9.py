import math
n=int(input())
a=list(map(int,input().split()))
b=[]
dp1=[]
dp2=[]
c=[]
d=[]
for i in range(n-1):
    b.append(abs((a[i+1]-a[i])))
for j in range(n-1): 
    if(j%2):
        c.append(b[j])
        d.append(-1*b[j])
    else:
        c.append(-1*b[j])
        d.append(b[j])

dp1.append(c[0])
dp2.append(d[0])

for i in range(1,n-1):
    dp1.append(max(c[i],dp1[i-1]+c[i]))
    dp2.append(max(d[i],dp2[i-1]+d[i]))
print(max(max(dp1),max(dp2)))

