def go(a,b):
    ret,c=0,a+b
    if d.get(c) and d[c]>0:
        d[c]-=1
        ret=go(b,c)+1
        d[c]+=1
    return ret

input()
d={}
for i in map(int,input().split()):
    if d.get(i):d[i]+=1
    else: d[i]=1

ans=2
for a in d:
    for b in d:
        if a!=b or d[a]>1:
            d[a]-=1
            d[b]-=1
            temp=go(a,b)+2
            ans=max(temp,ans)
            d[a]+=1
            d[b]+=1
print(ans)

