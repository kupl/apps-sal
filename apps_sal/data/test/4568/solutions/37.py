N = int(input())
S = list(input())
res = []
for i in range(1, N):
    res.append(len(set(S[:i]) & set(S[i:])))
print(max(res))
