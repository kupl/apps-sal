import itertools

N=int(input())
D=list(map(int, input().split()))

takocombi=list(itertools.combinations([i for i in range(N)],2))

ans=0
for h in range(len(takocombi)):
	ans+=D[takocombi[h][0]]*D[takocombi[h][1]]

print(ans)
