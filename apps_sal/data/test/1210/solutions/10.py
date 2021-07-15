from math import floor,ceil
def mults(a,b,n):
    return max(floor(b/n)-ceil(a/n)+1,0)
def prob(a,b,n):
    return 1-(mults(a,b,n))/(b-a+1)
ans=0
n,p=(list(map(int,input().split())))
firststart,firstend=(list(map(int,input().split())))
prevstart=firststart
prevend=firstend
for i in range(1,n):
    nextstart,nextend=(list(map(int,input().split())))
    ans+=(1-prob(prevstart,prevend,p)*prob(nextstart,nextend,p))
    prevstart=nextstart
    prevend=nextend
ans+=1-prob(prevstart,prevend,p)*prob(firststart,firstend,p)
print(2000*ans)

