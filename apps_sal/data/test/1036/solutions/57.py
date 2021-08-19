t = input
(N, K) = map(int, t().split())
S = t() * 2
W = 'P_PSRRS'
for k in range(K):
    T = ''
    for i in range(N):
        T += W[ord(S[i * 2]) + ord(S[i * 2 + 1]) - 160]
    S = T * 2
print(S[0])
