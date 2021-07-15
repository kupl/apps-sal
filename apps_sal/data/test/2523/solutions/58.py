S = input()
n = len(S)    
K = n
for k in range(n-1):
    if S[k] != S[k+1]:
        K = min(K, max(k+1, n-k-1))
print(K)

