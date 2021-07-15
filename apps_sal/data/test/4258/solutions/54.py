A,B,T=map(int, input().split())

ans=0
for i in range(1,21):
	if A*i <T+0.5:
		ans+=B

print(ans)
