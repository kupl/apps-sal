N,K = ( int(x) for x in input().split() )
walklist = [int(x) for x in input().split()]
cost = 0
for i in range(1,N):
	if walklist[i] + walklist[i-1] < K:
		cost += K - (walklist[i] + walklist[i-1])
		walklist[i] = K - walklist[i-1] 

print(cost)
print(" ".join([str(x) for x in walklist]))

