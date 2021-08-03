N, X = list(map(int, input().split()))
M = [0 for _ in range(N)]
for i in range(N):
    M[i] = int(input())

X -= (sum(M))
ans = len(M)

ans += (X // min(M))
print(ans)
