N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
D = [0] * N
for i in range(N):
	t = V[i] - C[i] 
	if t > 0:
		D[i] = t 
print((sum(D)))

