(N, M) = map(int, input().split())
A = [input() for i in range(N)]
B = ''.join([input() for i in range(M)])
f = 0
for i in range(N - M + 1):
    for j in range(N - M + 1):
        if ''.join([A[l][j:j + M] for l in range(i, i + M)]) == B:
            f = 1
print(['No', 'Yes'][f])
