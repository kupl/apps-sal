"""
created by shhuan at 2018/10/20 22:37

"""

"""
"""


N, M = list(map(int, input().split()))

A = []
loc = [{} for _ in range(M)]
for i in range(M):
    a = [int(x) for x in input().split()]
    A.append(a)
    for iv, v in enumerate(a):
        loc[i][v] = iv

ans = 0
ls = [0] * M
i = 0
while i < N:
    v = A[0][i]
    ls = [loc[j][v] for j in range(M)]
    segl = 1

    while all([l + segl < N for l in ls]) and all(A[il][l + segl] == A[0][ls[0] + segl] for il, l in enumerate(ls)):
        segl += 1
    ans += segl * (segl + 1) // 2
    i += segl


print(ans)
