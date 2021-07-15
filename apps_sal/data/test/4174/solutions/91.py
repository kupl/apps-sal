N,X=map(int,input().split())
L=list(map(int, input().split()))

D=0

for i in range(N):
	D+=L[i]
	if D>X:
		print(i+1)
		return
		
print(i+2)
