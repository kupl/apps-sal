n,p=list(map(int,input().split()))
s=list(input())

from itertools import groupby

gr = groupby(s)

cum=[]
tmp=0
for k,v in gr:
    if k=='0':
        cum.append(tmp+len(list(v)))
        tmp=0
    elif k=='1':
        tmp+=len(list(v))


cum = list(reversed(cum))

ans = 0
cnt = 0
tmp=0
gr = groupby(s)
for k,v in gr:
    if k=='0':
        cnt+=1
        if cnt>p:
            tmp -=cum.pop()

    tmp +=len(list(v))
    ans = max(ans,tmp)


print(ans)


