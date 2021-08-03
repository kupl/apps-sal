N, X = list(map(int, input().split()))
M = [int(input()) for _ in range(N)]
ans = N
for i in range(len(M)):
    X -= M[i]
ans += X // min(M)
print(ans)
