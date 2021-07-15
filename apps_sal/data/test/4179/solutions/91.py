n,m,c=list(map(int,input().split()))
B=list(map(int,input().split()))

cut = 0
for i in range(n):
	A = list(map(int,input().split()))
	ans = 0
	for i in range(m):
		ans += A[i]*B[i]
	if ans  > -c:
		cut += 1

print(cut)

