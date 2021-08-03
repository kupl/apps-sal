N, K = map(int, input().split())
alpha = list(map(int, input().split()))

alpha = sorted(alpha)
ans = N
t = 0

for i in range(N - 1, -1, -1):
    if t + alpha[i] < K:
        t += alpha[i]
    else:
        ans = min(ans, i)

print(ans)
