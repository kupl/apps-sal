S = input()
N = len(S)
res = N
for i in range(N - 1):
    if S[i] != S[i + 1]:
        res = min(res, max(i + 1, N - (i + 1)))
print(res)
