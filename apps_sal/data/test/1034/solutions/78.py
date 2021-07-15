import heapq
X, Y, Z, K = map(int,input().split())
A = list(map(lambda x: -1 * int(x),input().split()))
B = list(map(lambda x: -1 * int(x),input().split()))
C = list(map(lambda x: -1 * int(x),input().split()))
A.sort()
B.sort()
C.sort()
Q = []
heapq.heappush(Q, (A[0] + B[0] + C[0], 0, 0, 0))
for _ in range(K):
    SUM, a, b, c = heapq.heappop(Q)
    print(-1 * SUM)
    if a <= X - 2 and not (A[a+1] + B[b] + C[c], a+1, b, c) in Q:
        heapq.heappush(Q, (A[a+1] + B[b] + C[c], a+1, b, c))
    if b <= Y - 2 and not (A[a] + B[b+1] + C[c], a, b+1, c) in Q:
        heapq.heappush(Q, (A[a] + B[b+1] + C[c], a, b+1, c))
    if c <= Z - 2 and not (A[a] + B[b] + C[c+1], a, b, c+1) in Q:
        heapq.heappush(Q, (A[a] + B[b] + C[c+1], a, b, c+1))
