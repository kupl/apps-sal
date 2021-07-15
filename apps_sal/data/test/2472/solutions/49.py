N=int(input())
P=[]
for i in range(N):
    a,b=map(int,input().split())
    P.append([b,a])
P=sorted(P)
time=0
for i in range(N):
    time+=P[i][1]
    if time>P[i][0]:
        print('No')
        return
print('Yes')
