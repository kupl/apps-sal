n = int(input())

s=input().split()

for i in range(n):
    s[i]=int(s[i])



ans=sum(s)
if(len(s)==1):
    print(1-s[0])
elif(s.count(0)==len(s)):
    print(len(s))
elif(s.count(1)==len(s)):
    print(sum(s)-1)
else:
    r=0
    if(s[0]==0):
       s=[1]+s
       r=1
    L=[0]
    for i in range(1,n+r):
        if(s[i]!=s[i-1]):
            L.append(i)
    L.append(n+r)
    m=len(L)
    maxx=0
    for i in range(2,m,2):
        ans=sum(s)-r+L[i]-L[i-1]
        e=ans
        for j in range(i+2,m,2):
            ans=ans+L[j]-L[j-1]-(L[j-1]-L[j-2])
            if(ans>e):
                e=ans            
        if(e>maxx):
            maxx=e
    print(maxx)
    
    

