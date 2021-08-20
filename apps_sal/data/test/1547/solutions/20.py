import sys
(n, m, k) = [int(x) for x in input().split()]
(L, C) = ([(-1, 0) for i in range(n)], [(-1, 0) for i in range(m)])
for (i, line) in enumerate(sys.stdin):
    (t, r, c) = [int(x) for x in line.split()]
    if t == 1:
        L[r - 1] = (i, c)
    else:
        C[r - 1] = (i, c)
matrix = [[max(L[i], C[j])[1] for j in range(m)] for i in range(n)]
for i in range(n):
    sys.stdout.write(' '.join(map(str, matrix[i])) + '\n')
