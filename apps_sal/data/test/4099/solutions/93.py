(N, K, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
score = 0
for i in range(N - 1):
    score += A[i]
ans = M * N - score
if 0 <= ans <= K:
    print(ans)
elif ans < 0:
    print(0)
else:
    print(-1)
