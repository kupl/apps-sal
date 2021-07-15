N = int(input())
M = 0
while (M + 1) * (M + 2) / 2 <= N :
	M += 1
print(M)
for i in range(1, M) :
	print(i, end = ' ')
	N -= i
print(N)	

