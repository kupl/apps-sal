(N, M) = map(int, input().split())
mat = [[int(i) for i in input().split()] for k in range(M)]
p = [int(i) for i in input().split()]
switch = [0] * N
O = [0] * M
L = [False] * M
ans = 0
for i in range(2 ** N):
    switchsub = list(format(i, 'b'))
    for j in range(len(switchsub)):
        switch[-j - 1] = switchsub[-j - 1]
    for j in range(N):
        if switch[j] == '1':
            for k in range(M):
                for l in range(1, len(mat[k])):
                    if mat[k][l] == j + 1:
                        O[k] += 1
    for j in range(M):
        if O[j] % 2 == p[j]:
            L[j] = True
    if False not in L:
        ans += 1
        switch = [0] * N
        O = [0] * M
        L = [False] * M
    if False in L:
        switch = [0] * N
        O = [0] * M
        L = [False] * M
print(ans)
