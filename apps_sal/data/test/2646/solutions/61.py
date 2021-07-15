from collections import deque
N,M=map(int,input().split())
haba=[[] for i in range(N+1)]
for i in range(M):
    A,B=map(int,input().split())
    haba[A].append(B)
    haba[B].append(A)
kyori=[-1]*(N+1)
kyori[0]=0
kyori[1]=0

que=deque()
que.append(1)

while que:
    kari=que.popleft()
    for i in haba[kari]:
        if kyori[i]!=-1:
            continue
        kyori[i]=kari
        que.append(i)

ans=kyori[2:]
print("Yes")
for i in range(len(ans)):
    print(ans[i])
