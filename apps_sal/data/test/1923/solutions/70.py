N = int(input())
L = map(int, input().split())

L = sorted(L)

Total = 0
for i in range(N*2):
	if(i%2==0):
		Total+=L[i]

print(Total)
