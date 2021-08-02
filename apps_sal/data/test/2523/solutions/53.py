S = input()
L = len(S)

ans = L
for i in range(1, L):
    if S[i - 1] != S[i]:
        ans = min(max(L - i, i), ans)
print(ans)
