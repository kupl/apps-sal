def light(l,i):
    k=1<<(i-1)
    if l&k:
        return 1
    else:
        return 0

N, M = map(int,input().split())
s=list()
for j in range(0,M):
    s.append(0)
for j in range(0,M):
    s[j]=list(map(int,input().split()))
p=list(map(int,input().split()))

a=0
for l in range(0,1<<N):
    b=0
    for j in range(0,M):
        c=0
        for i in range(1,s[j][0]+1):
            c+=light(l,s[j][i])
        if c%2==p[j]:
            b+=1
    if b==M:
        a+=1
print(a)
