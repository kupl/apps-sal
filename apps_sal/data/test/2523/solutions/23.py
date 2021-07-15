S = input()
L = len(S)
K = L
for i in range(1, L):
    if S[i-1] != S[i]:
        K = min(K, max(i, L - i))
print(K)

