mex = [[1, 2, 1], [2, 0, 0], [1, 0, 0]]
(N, *I) = map(int, open(0).read().split())
A = [I[:N]]
for (i, a) in enumerate(I[N:], 1):
    M = N if i < 4 else min(4, N)
    Ai = [a]
    for j in range(1, M):
        Ai.append(mex[A[-1][j]][Ai[-1]])
    A.append(Ai)
ans = [0, 0, 0]
for (i, Ai) in enumerate(A):
    for (j, aij) in enumerate(Ai):
        ans[aij] += N - max(i, j) if i >= 3 and j >= 3 else 1
print(*ans)
