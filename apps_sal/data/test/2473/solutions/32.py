N,K = map(int,input().split())
ary = [list(map(int,input().split())) for _ in range(N)]
a = sorted(ary)
ans = float("Inf")
for i in range(N-K+1):
    for j in range(i,N-K+1):
        lx = a[i][0]; rx = a[K+j-1][0]
        b = a[i:K+j]
        c = sorted(b,key=lambda x:(x[1]))
        for k in range(len(c)-K+1):
            by = c[k][1]; uy = c[k+K-1][1]
            ans = min(ans,(rx - lx) * (uy - by))
print(ans)
