li=[]
N,M=list(map(int,input().split()))

for i in range(N):
    a,b=list(map(int,input().split()))
    li.append([a,b])

li.sort()

g=0
s=0

for i in range(N):
    if li[i][1]+s<M:
        s+=li[i][1]
        g+=li[i][1]*li[i][0]
    else:
        g+=(M-s)*li[i][0]
        print(g)
        return

