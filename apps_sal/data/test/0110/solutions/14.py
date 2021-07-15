n=int(input())
l = list(map(int, input().split()))
t = 0
ind = -1
c=0
for i in range(n):
    if l[i] >=0: l[i] = -l[i]-1
    if l[i]<0:c=c+1
    if l[i]<=0 and l[i]<t:
        t = l[i]
        ind=i
if c%2==0:print(*l)
else:
    l[ind]=-l[ind]-1
    print(*l)

