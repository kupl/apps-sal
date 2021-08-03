N = int(input())
S = list(input())
e, w = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    w[i] += w[i - 1] + (1 if S[i - 1] == 'W' else 0)
    e[i] += e[i - 1] + (1 if S[i - 1] == 'E' else 0)
ans = N
for i in range(N):
    ans = min(ans, w[i] + e[-1] - e[i + 1])
print(ans)
