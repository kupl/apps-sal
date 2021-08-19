(N, K) = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for (i, j) in zip(range(N - 1), range(1, N)):
    Asum = A[i] + A[j]
    if Asum <= K:
        continue
    eat = Asum - K
    d = min(eat, A[j])
    A[j] -= d
    eat -= d
    ans += d
    d = min(eat, A[i])
    A[i] -= d
    ans += d
print(ans)
