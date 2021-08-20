from heapq import heapify, heappop, heappush
(X, Y, Z, K) = map(int, input().split())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()), reverse=True)
C = sorted(map(int, input().split()), reverse=True)
que = [[-(A[0] + B[0] + C[0]), 0, 0, 0]]
heapify(que)
s = set()
for i in range(K):
    p = heappop(que)
    print(-p[0])
    if p[1] < X - 1 and (not (p[1] + 1, p[2], p[3]) in s):
        heappush(que, [-sum([A[p[1] + 1], B[p[2]], C[p[3]]]), p[1] + 1, p[2], p[3]])
        s.add((p[1] + 1, p[2], p[3]))
    if p[2] < Y - 1 and (not (p[1], p[2] + 1, p[3]) in s):
        heappush(que, [-sum([A[p[1]], B[p[2] + 1], C[p[3]]]), p[1], p[2] + 1, p[3]])
        s.add((p[1], p[2] + 1, p[3]))
    if p[3] < Z - 1 and (not (p[1], p[2], p[3] + 1) in s):
        heappush(que, [-sum([A[p[1]], B[p[2]], C[p[3] + 1]]), p[1], p[2], p[3] + 1])
        s.add((p[1], p[2], p[3] + 1))
