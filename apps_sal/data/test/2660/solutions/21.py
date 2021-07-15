import heapq

q = int(input())
l = []
r = []
ans = 0

for i in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        ans += a[2]
        if l == []:
            heapq.heappush(r,a[1])
            heapq.heappush(l,-a[1])
        else: 
            ll = -heapq.heappop(l)
            rr = heapq.heappop(r)
            if ll <= a[1] <= rr:
                heapq.heappush(r,rr)
                heapq.heappush(l,-ll) 
                heapq.heappush(r,a[1])
                heapq.heappush(l,-a[1]) 

            elif ll > a[1]:
                ans += ll-a[1]
                heapq.heappush(r,rr)
                heapq.heappush(r,ll) 
                heapq.heappush(l,-a[1])
                heapq.heappush(l,-a[1]) 
            else:
                ans += a[1] -rr
                heapq.heappush(l,-rr)
                heapq.heappush(l,-ll) 
                heapq.heappush(r,a[1])
                heapq.heappush(r,a[1]) 
        
    else:
        a = heapq.heappop(l)
        print(-a,ans)
        heapq.heappush(l,a)
