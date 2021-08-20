(N, K) = map(int, input().split())
p = list(map(int, input().split()))
for i in range(N):
    p[i] = (1 + p[i]) / 2
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + p[i]
'\nS[0] = 0\nS[1] = p[0]\nS[2] = p[0] + p[1]\nS[N] = p[0] + ... + p[N-1]\n \nS[K]-S[0] = p[K-1] + ... + p[0]\nS[K+1]-S[1] = p[K] + ... + p[1]\nS[K+2]-S[2] = p[K+1] + ... + p[2]\nS[N]-S[N-K] = p[N-1] + ... + p[N-K]\n'
ans = 0
for i in range(N - K + 1):
    ans = max(ans, S[i + K] - S[i])
print(ans)
