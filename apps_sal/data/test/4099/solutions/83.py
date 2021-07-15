N,K,M = map(int,input().split())
A = [int(i) for i in input().split()]
ans = M*N
for i in range(N-1):
    ans -= A[i]
if(ans > K):
    print(-1)
    return
if(ans <= 0):
    print(0)
    return
print(ans)
