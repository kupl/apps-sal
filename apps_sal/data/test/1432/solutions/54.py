N = int(input())
A = list(map(int,input().split()))
ans = [0]*N
ans[0] = sum([(-1)**i*A[i] for i in range(N)])
for i in range(1,N):
    ans[i] = 2*A[i-1]-ans[i-1]
print(*ans)
