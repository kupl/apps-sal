import heapq
N,K=map(int,input().split())
TD=[list(map(int,input().split())) for _ in range(N)]
TD.sort(key=lambda x:x[1], reverse=True)

NETA=set()
duplication=[]
heapq.heapify(duplication)
ans=0
for t,d in TD[:K]:
    if t in NETA:
        heapq.heappush(duplication,d)
    else:
        NETA.add(t)
    ans+=d

s=[-float("inf")]*(K+1)
cnt=len(NETA)
s[cnt]=ans
for t,d in TD[K:]:
    if t in NETA:
        continue
    else:
        if duplication:
            x=heapq.heappop(duplication)
            ans+=d-x
            NETA.add(t)
            cnt+=1
            s[cnt]=ans

for i in range(K+1):
    s[i]+=i*i
print(max(s))
