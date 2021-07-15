def resolve():    
    import heapq
    n,m=map(int,input().split())
    ab=[list(map(int,input().split())) for _ in range(n)]
    b=[[] for _ in range(10**5+1)]
    for i,j in ab:
        b[i].append(-j)
    q=[]
    ans=0
    for i in range(1,m+1):
        for j in b[i]:
            heapq.heappush(q,j)
        if q:
            ans+=heapq.heappop(q)
    print(-ans)
        
def __starting_point():
    resolve()
__starting_point()
