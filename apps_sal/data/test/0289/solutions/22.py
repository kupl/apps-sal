def f(S):
    ans = 0
    for i in range(1, len(S)):
        if S[i - 1] == 'V' and S[i] == 'K':
            ans += 1
    return ans


S = list(input())
ans = f(S)
D = {'V': 'K', 'K': 'V'}
for i in range(len(S)):
    S[i] = D[S[i]]
    ans = max(ans, f(S))
    S[i] = D[S[i]]
print(ans)
