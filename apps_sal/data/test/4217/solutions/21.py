N,M=map(int, input().split())
ans=set(list(map(int, input().split()))[1:])

for i in range(N-1):
	temp=set(list(map(int, input().split()))[1:])
	ans=ans&temp

print(len(ans))
