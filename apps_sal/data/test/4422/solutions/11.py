(N, K) = input().strip().split()
S = input()
N = int(N)
K = int(K)
S = list(S)
if S[K - 1] == 'A':
    S[K - 1] = 'a'
elif S[K - 1] == 'B':
    S[K - 1] = 'b'
else:
    S[K - 1] = 'c'
print(''.join(S))
