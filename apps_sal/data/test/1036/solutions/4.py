(N, K) = map(int, input().split())
s = input()
S = s * 4
D = {}
D['R', 'R'] = 'R'
D['R', 'S'] = 'R'
D['S', 'R'] = 'R'
D['S', 'S'] = 'S'
D['S', 'P'] = 'S'
D['P', 'S'] = 'S'
D['P', 'P'] = 'P'
D['P', 'R'] = 'P'
D['R', 'P'] = 'P'
for i in range(K):
    A = ''
    for j in range(len(S) // 2):
        A += D[S[2 * j], S[2 * j + 1]]
    S = A * 2
print(S[0])
