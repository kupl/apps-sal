from heapq import heappop, heappush

N, Q = list(map(int, input().split()))

M = 2 * (10 ** 5)
belong = [None] * N
rate = [None] * N
kdgt = [[] for _ in range(M)]

for c in range(N):
    A, B = list(map(int, input().split()))
    B -= 1
    belong[c] = B
    rate[c] = A
    heappush(kdgt[B], (-A, c))

q = []

for i in range(M):
    if kdgt[i]:
        A, c = kdgt[i][0]
        heappush(q, (-A, c, i))

for _ in range(Q):
    C, D = list(map(int, input().split()))
    C -= 1
    D -= 1
    pd = belong[C]
    belong[C] = D

    while kdgt[pd]:
        A, c = kdgt[pd][0]
        if belong[c] != pd:
            heappop(kdgt[pd])
        else:
            heappush(q, (-A, c, pd))
            break

    heappush(kdgt[D], (-rate[C], C))
    while kdgt[D]:
        A, c = kdgt[D][0]
        if belong[c] != D:
            heappop(kdgt[D])
        else:
            heappush(q, (-A, c, D))
            break

    while q:
        A, c, d = q[0]

        if belong[c] != d or kdgt[d][0][1] != c:
            heappop(q)
        else:
            print(A)
            break
