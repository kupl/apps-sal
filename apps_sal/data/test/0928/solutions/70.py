N,K = map(int,input().split())
A = [int(i) for i in input().split()]
ans = 0
r = 0
l = 0
s = 0
for r in range(N) :
    s += A[r]
    while s >= K : 
        ans += N-r
        s -= A[l]
        l += 1
        
print(ans)
