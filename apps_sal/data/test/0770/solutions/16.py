n=int(input())
s=list(map(int,input().split()))
f=[]
i=0
while i<n and s[i]!=1:
    i+=1
if i==n:
    print(0)
else:
    ans=1
    while i<n:
        if s[i]==1:
            l=0
            while i<n-1 and s[i+1]==0:
                l+=1
                i+=1
            if i<n-1:
                f.append(l)
        i+=1
    i=0
    while i<len(f):
        if f[i]==0:
            ans+=1
        else:
            ans+=2
        i+=1
    print(ans)
        

