N,K=map(int,input().split())
V=list(map(int,input().split()))
import heapq
turn=min(N,K)
m=0
for A in range(turn+1):
  for B in range(turn+1-A):
    h=[]
    heapq.heapify(h)
    if A>0:
      h=V[:A]+h
    if B>0:
      h=h+V[len(V)-B:]
    heapq.heapify(h)  

    ans=sum(h)
    for i in range(K-A-B):
      if h!=[]:
        f=heapq.heappop(h)
 
        if f<0:
          ans-=f
    m=max(ans,m)


    
print(m)   
