h,w,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
ch,cw=[0]*(h+1),[0]*(w+1)
for x in l:
    ch[x[0]]+=1
    cw[x[1]]+=1
Mh,Mw=max(ch),max(cw)
n0=ch.count(Mh)*cw.count(Mw)
cnt=0
for x in l:
    if ch[x[0]]==Mh and cw[x[1]]==Mw:cnt+=1
ans=Mh+Mw-1
if cnt<n0:ans+=1
print(ans)
