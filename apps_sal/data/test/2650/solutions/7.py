from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

N, Q = list(map(int, input().split()))

S = []
PQs = [[] for _ in range(200000)]
T = [0] * 200000
M = []
for n in range(N):
    a, b = list(map(int, input().split()))
    S.append([a, b - 1])
    PQs[b - 1] += [(-a, n)]

for b in range(200000):
    if len(PQs[b]) > 0:
        heapify(PQs[b])
        M.append((-PQs[b][0][0], b, 0))
heapify(M)


ans = []
for q in range(1, Q + 1):
    c, d = list(map(int, input().split()))
    d = d - 1
    d_prv = S[c - 1][1]
    S[c - 1][1] = d

    heappush(PQs[d], (-S[c - 1][0], c - 1))
    while d != S[PQs[d][0][1]][1]:
        heappop(PQs[d])
    if -PQs[d][0][0] == S[c - 1][0]:
        heappush(M, (-PQs[d][0][0], d, q))
        T[d] = q

    if len(PQs[d_prv]) > 0:
        while d_prv != S[PQs[d_prv][0][1]][1]:
            heappop(PQs[d_prv])
            if len(PQs[d_prv]) == 0:
                break

        if len(PQs[d_prv]) > 0 and -PQs[d_prv][0][0] < S[c - 1][0]:
            heappush(M, (-PQs[d_prv][0][0], d_prv, q))

        if len(PQs[d_prv]) == 0 or -PQs[d_prv][0][0] < S[c - 1][0]:
            T[d_prv] = q

    while M[0][2] != T[M[0][1]]:
        heappop(M)

    ans.append(M[0][0])


print(('\n'.join(map(str, ans))))
