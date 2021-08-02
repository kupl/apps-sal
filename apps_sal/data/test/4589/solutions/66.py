h, w = list(map(int, input().split()))
S = [input() for _ in range(h)]
S = ['.' + s + '.' for s in S]
S = ['.' * (w + 2)] + S + ['.' * (w + 2)]
for i in range(1, h + 1):
    l = ''
    for j in range(1, w + 1):
        if S[i][j] == '#':
            l += '#'
        else:
            l += str([S[i - 1][j - 1], S[i - 1][j], S[i - 1][j + 1], S[i][j + 1], S[i + 1][j + 1], S[i + 1][j], S[i + 1][j - 1], S[i][j - 1]].count('#'))
    print(l)
