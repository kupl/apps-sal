N, K = [int(_) for _ in input().split()]
S = list(input())
g = {}
g['R', 'R'] = 'R'
g['R', 'P'] = 'P'
g['R', 'S'] = 'R'
g['P', 'R'] = 'P'
g['P', 'P'] = 'P'
g['P', 'S'] = 'S'
g['S', 'R'] = 'R'
g['S', 'P'] = 'S'
g['S', 'S'] = 'S'
for _ in range(K):
    S *= 2
    S = [g[a, b] for a, b in zip(S[::2], S[1::2])]
print((S[0]))
