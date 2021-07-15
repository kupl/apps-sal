import heapq
N,Q=map(int,input().split())
M=2*(10**5)
belong=[]
rate=[]
garden=[[]for _ in range(M)]
for c in range(N):
    A,B=map(int,input().split())
    B-=1
    belong.append(B)
    rate.append(A)
    heapq.heappush(garden[B],(-A,c))
    
strong=[]

for i in range(M):
    if garden[i]:
        A,c=garden[i][0]
        heapq.heappush(strong,(-A,c,i))
        
for i in range(Q):
    C,D=map(int,input().split())
    C-=1
    D-=1
    now=belong[C]
    belong[C]=D
    
    while garden[now]:
        A,c=garden[now][0]
        if belong[c]!=now:
            heapq.heappop(garden[now])
        else:
            heapq.heappush(strong,(-A,c,now))
            break
            
    heapq.heappush(garden[D],(-rate[C],C))
    while garden[D]:
        A,c=garden[D][0]
        heapq.heappush(strong,(-A,c,D))
        break
    
    while strong:
        A,c,d=strong[0]
        if belong[c]!=d or garden[d][0][1]!=c:
            heapq.heappop(strong)
        else:
            print(A)
            break
