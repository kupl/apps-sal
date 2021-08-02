import sys
input = sys.stdin.readline

M, N, K, T = map(int, input().split())
A = list(map(int, input().split()))
LRD = [list(map(int, input().split())) for _ in range(K)]

A.append(10**15)
A.sort(reverse=True)

l = 0
r = M + 1
while r - l > 1:
    m = (r + l) // 2
    D_limit = A[m]

    P = [0] * (N + 2)
    for L, R, D in LRD:
        if D_limit < D:
            P[L] += 1
            P[R + 1] -= 1
    c = 0
    for i in range(N + 1):
        P[i + 1] += P[i]
        if P[i + 1] > 0:
            c += 1
    #print(P, m)
    time = N + 1 + 2 * c
    # print(time)

    if time <= T:
        l = m
    else:
        r = m

print(l)
