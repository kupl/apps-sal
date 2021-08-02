S = input()
N = len(S)
ans = N

for n in range(N - 1):
    if S[n + 1] != S[n]:
        ans = min(ans, max(n + 1, N - n - 1))

print(ans)
