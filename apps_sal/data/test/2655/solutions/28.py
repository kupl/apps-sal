N = int(input())
A = list(map(int,input().split()))
A.sort()
ans = 0
for k in range(1, N): ans += A[N-k//2-1]
print(ans)
