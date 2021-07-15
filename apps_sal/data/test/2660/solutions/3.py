from heapq import heappop,heappush
l,r=[],[]
ans=0
for _ in range(int(input())):
	a=list(map(int,input().split()))
	if a[0]==1:
		_,ia,ib=a
		heappush(l,-ia)
		heappush(r,ia)
		ll=heappop(l)
		rr=heappop(r)
		heappush(l,-rr)
		heappush(r,-ll)
		ans+=ib+abs(ll+rr)
	else:print(-l[0],ans)
