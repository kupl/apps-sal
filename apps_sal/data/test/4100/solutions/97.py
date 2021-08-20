import bisect as bi
(N, K, Q) = map(int, input().split())
A = [int(input()) for i in range(Q)]
B = [K] * N
p = 0
for i in range(N + 1):
    A.append(i + 1)
C = sorted(A)
for i in range(N):
    B[i] += bi.bisect_left(C, i + 2) - p - 1
    p = bi.bisect_left(C, i + 2)
for i in range(N):
    if B[i] > Q:
        print('Yes')
    else:
        print('No')
