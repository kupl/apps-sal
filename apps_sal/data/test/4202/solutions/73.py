import itertools

L,R=map(int, input().split())

for i in range((2*10**9)//2019+1):
	if L<=i*2019 and i*2019<=R:
		print(0)
		return

ans=2020

for h in range(L,R+1):
	for g in range(h+1,R+1):
		ans=min(ans,(h*g)%2019)

print(ans)
