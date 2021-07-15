s=input()
k=int(input())

s+='?'*k
n=len(s)
best=0
for i in range(n):
    for j in range(i+1,n):
        if((j-i+1)%2!=0):
            continue
        x=j-i+1
        valid=True
        for e in range(i,j+1):
            if(e+x//2>j):
                break
            if(s[e]=='?' or s[e+x//2]=='?'  or s[e]==s[e+x//2]):
                continue
            valid=False
        if(valid):
            best=max(best,x)
print(best)

