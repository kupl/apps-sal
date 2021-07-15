N,K,Q=list(map(int, input().split()))
A=[int(input()) for _ in range(Q)]
party=[-Q+K]*N

for a in A:
	party[a-1]+=1

for p in party:
	if p>0:
		print("Yes")
	else:
		print("No")

