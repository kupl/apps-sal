import heapq
N,M=map(int,input().split())
AB=[[]for i in range(10**5+1)]
for i in range(N):
    a,b=map(int,input().split())
    AB[a].append(-b)
q=[]
heapq.heapify(q)
ans=0
for i in range(1,M+1):
    for b in AB[i]:
        heapq.heappush(q,b)
    if len(q)>0:
        ans+=-heapq.heappop(q)
print(ans)
