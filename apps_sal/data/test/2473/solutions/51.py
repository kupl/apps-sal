N,K = list(map(int,input().split()))
p = sorted([list(map(int,input().split())) for _ in range(N)])
x, y = list(zip(*p))
inf = float('inf')
ans = inf

for i in range(N-K+1):
    for j in range(K+i-1, N):
        Ys = sorted(y[i:j+1])
        for k in range(len(Ys)-K+1):
            ans = min(ans, (x[j]-x[i])*(Ys[k+K-1]-Ys[k]))
print(ans)

