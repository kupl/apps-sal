(N, K) = map(int, input().split())
S = str(input())
score = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        score += 1
ans = min(score + 2 * K, N - 1)
print(ans)
