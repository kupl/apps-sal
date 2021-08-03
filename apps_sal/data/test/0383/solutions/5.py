import sys

f = sys.stdin
n, k, d = list(map(int, f.readline().strip().split()))

Nd = [[1] * (n + 1), [1] * (n + 1)]
Nd[1][0] = 0
Nd[1][1] = 0

for i in range(2, n + 1):
    N = 0
    for j in range(1, k + 1):
        if i >= j:
            N += Nd[0][i - j]
    Nd[0][i] = N

    # if i==2: continue
    N = 0
    for j in range(1, k + 1):
        if i >= j:
            if j >= d:
                N += Nd[0][i - j]
            else:
                N += Nd[1][i - j]
    Nd[1][i] = N

    # print(Nd)

if d > 1:
    print(Nd[1][n] % 1000000007)
else:
    print(Nd[0][n] % 1000000007)
