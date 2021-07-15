N,D = map(int,input().split())
X = [[int(i) for i in input().split()] for j in range(N)]
ans = 0

for i in range(N):
    for j in range(i+1,N):
        L = 0
        for k in range(D):
            L += (X[i][k] - X[j][k]) ** 2
        M = L ** 0.5
        if(M == int(M)):
            ans += 1

print(ans)
