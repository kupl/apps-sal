n=int(input())
l=sorted(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d={}
for x in l:
    d[x]=d.get(x,0)+1
ans=(0,0,0)
for i in range(m):
    cob=d.get(b[i],0)
    coc=d.get(c[i],0)
    if cob>ans[1]: ans=(i,cob,coc)
    if cob==ans[1] and coc>ans[2]: ans=(i,cob,coc)
print(ans[0]+1)
