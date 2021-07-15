import math
import sys
input=sys.stdin.readline
 
p=(10**9)+7
pri=p
fac=[1 for i in range((10**6)+1)]
for i in range(2,len(fac)):
    fac[i]=(fac[i-1]*(i%pri))%pri
def modi(x):
    return (pow(x,p-2,p))%p;
    
def ncr(n,r):
    x=(fac[n]*((modi(fac[r])%p)*(modi(fac[n-r])%p))%p)%p
    return x;

def prime(x):
    ans=[]
    while(x%2==0):
        x=x//2
        ans.append(2)
    for i in range(3,int(math.sqrt(x))+1,2):
        while(x%i==0):
            ans.append(i)
            x=x//i
    if(x>2):
        ans.append(x)

    return ans;



n=int(input())

z=list(map(int,input().split()))
ans=[]
for i in range(len(z)):
    m=prime(z[i])
    ans.extend(m)
  
ans.sort()
if(ans.count(1)==len(ans)):
    print(1)
    return
cn=[]
count=1
for i in range(1,len(ans)):
    if(ans[i]==ans[i-1]):
        count+=1
    else:
        cn.append(count)
        count=1
cn.append(count)
al=1

for i in range(len(cn)):
    al=al*ncr(n+cn[i]-1,n-1)
    al%=pri
print(al)
    
    

