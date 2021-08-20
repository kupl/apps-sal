from itertools import product
[N, M, X] = [int(i) for i in input().split()]
bk = [[int(i) for i in input().split()] for _ in range(N)]
ans = 12 * 10 ** 5 + 1
for seq in product(range(2), repeat=N):
    S = [0] * (M + 1)
    for i in range(N):
        for j in range(M + 1):
            S[j] += seq[i] * bk[i][j]
    if min(S[1:M + 1]) >= X:
        ans = min(ans, S[0])
if ans == 12 * 10 ** 5 + 1:
    print(-1)
else:
    print(ans)
