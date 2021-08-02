S = input()
K = int(input())
N = len(S)
s = set()
for i in range(N):
    for j in range(i + 1, min(i + K + 1, N + 1)):
        s |= {S[i:j]}
A = list(s)
A.sort()
print((A[K - 1]))
