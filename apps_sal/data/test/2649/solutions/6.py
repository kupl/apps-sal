n=int(input())
zp=[]
zl=[]
for i in range(n):
    a,b=map(int,input().split())
    zp.append(a+b)
    zl.append(a-b)
ans=max((max(zp)-min(zp)),(max(zl)-min(zl)))
print(ans)
