N=int(input())
a=list(map(int,input().strip().split()))
d={}

for n in range(N):
    if d.get(a[n])==None:
        d[a[n]]=1
    else:
        d[a[n]]+=1

cnt=0
for key in list(d.keys()):
    if key>d[key]:
        cnt+=d[key]
    else:
        cnt+=d[key]-key

print(cnt)

