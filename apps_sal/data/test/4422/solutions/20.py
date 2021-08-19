(N, K) = list(map(int, input().split()))
S = list(input())
if S[K - 1] == 'A':
    S[K - 1] = 'a'
elif S[K - 1] == 'B':
    S[K - 1] = 'b'
elif S[K - 1] == 'C':
    S[K - 1] = 'c'
''.join(S)
S_1 = S[0]
for i in range(1, N):
    S_1 = S_1 + S[i]
print(S_1)
