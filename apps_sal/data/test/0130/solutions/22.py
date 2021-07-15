n, m = list(map(int,input().split()))
q = [str(input()) for i in range(n)]
k=0
t=True
u=0
li=vi=n*m
pi=ni=0
for i in range(n):
    t=False
    u=0
    for j in q[i]:
        if j=='B':
            if u<li:
                li=u
            if u>pi:
                pi=u
            if i<vi:
                vi=i
            if i>ni:
                ni=i
            k+=1
        u+=1
if (max(ni-vi, pi-li)+1)>n or (max(ni-vi, pi-li)+1)>m:
    print(-1)
elif k==0:
    print(1)
else:
    print((max(ni-vi, pi-li)+1)**2-k)

