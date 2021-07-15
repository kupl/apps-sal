from collections import deque
N,M=map(int,input().split())
adjacent=[set() for x in range(N)]
for m in range(M):
    A,B=map(int,input().split())
    adjacent[A-1].add(B-1)
    adjacent[B-1].add(A-1)
ans=[0]*N
deque1=deque()
already=set()
already.add(0)
num_already=1
for j in adjacent[0]:
    deque1.append(j)
    already.add(j)
    num_already+=1
    ans[j]=1
while(num_already!=N):
    now=deque1.popleft()
    for k in adjacent[now]:
        if k not in already:
            num_already+=1
            already.add(k)
            ans[k]=now+1
            deque1.append(k)
print("Yes")
for i in range(1,N):
    print(ans[i])
