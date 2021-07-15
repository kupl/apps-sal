N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
	A[i] = A[i]*(i+1)*(N-i)

A.sort()
B.sort()

ans = 0
for i in range(N):
	ans = ans + (A[i]*B[N-i-1])%998244353

print(ans%998244353)

