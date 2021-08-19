from numpy import *
(N, M, X) = map(int, input().split())
B = [array(list(map(int, input().split())), uint32) for _ in range(N)]
c = inf
for i in range(2 ** N):
    a = zeros(M + 1, uint32)
    j = 0
    while i:
        if i & 1:
            a += B[j]
        i >>= 1
        j += 1
    (C, *A) = a
    if min(A) >= X:
        c = min([c, C])
print(c if c < inf else -1)
