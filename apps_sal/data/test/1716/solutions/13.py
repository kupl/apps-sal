from itertools import accumulate
(N, M, Q) = map(int, input().split())
a = [[0] * N for i in range(N)]
for i in range(M):
    (l, r) = map(int, input().split())
    a[l - 1][r - 1] += 1
for i in range(N):
    a[i] = list(accumulate(a[i]))
for i in range(N):
    for j in range(N - 1):
        a[j + 1][i] += a[j][i]
for i in range(Q):
    (p, q) = map(int, input().split())
    if p == 1:
        ans = a[q - 1][q - 1]
    else:
        ans = a[q - 1][q - 1] - a[p - 2][q - 1]
    print(ans)
