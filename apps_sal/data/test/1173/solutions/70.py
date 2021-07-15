def opp(i):  #対戦希望相手
    return a[i][nex[i]]

from sys import stdin
#入力
readline=stdin.readline
n=int(readline())
m=n*(n-1)//2
a=[list(map(lambda x:int(x)-1,readline().split())) for _ in range(n)]

nex=[0]*n
before=set(range(n))
day=0
for day in range(1,m+1):
    now=set()
    while len(before)>0:
        p=before.pop()
        q=opp(p)
        if opp(q)==p and p not in now and q not in now:
            nex[p]+=1
            nex[q]+=1
            if nex[p]<n-1:
                now.add(p)
            if nex[q]<n-1:
                now.add(q)
            if q in before:
                before.remove(q)
    before=now
    if len(before)==0:
        break

if min(nex)==n-1:
    print(day)
else:
    print(-1)
