import sys
S = sys.stdin.read()
S = list([list(map(int, x)) for x in list([x.split() for x in [x for x in S.split('\n') if len(x) > 1]])])
n, k, x, B = S[0][0], S[0][1], S[0][2], S[1]

X = [[-1 for i in range(x + 1)] for i in range(n + 1)]
X[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, x + 1):
        X[i][j] = max([X[i][j], max([-1] + [X[i - l][j - 1] + B[i - 1] for l in range(1, min([i, k]) + 1) if X[i - l][j - 1] != -1])])
print(max(list(map(max, X[n - k + 1:n + 1]))))
