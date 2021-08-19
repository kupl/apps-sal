import heapq
N = int(input())
A = list(map(int, input().split()))
S = []
P = A[:N]
Q = A[2 * N:]
for i in range(N):
    Q[i] *= -1
R = A[N:2 * N]
p = [0] * (N + 1)
q = [0] * (N + 1)
heapq.heapify(P)
heapq.heapify(Q)
sp = sum(P)
sq = sum(Q)
p[0] = sp
q[0] = sq
for i in range(1, N + 1):
    heapq.heappush(P, R[i - 1])
    x = heapq.heappop(P)
    heapq.heappush(Q, -R[-i])
    y = heapq.heappop(Q)
    sp = sp + R[i - 1] - x
    sq = sq - R[-i] - y
    p[i] = sp
    q[i] = sq
ans = -10 ** 100
for k in range(N + 1):
    ans = max(ans, p[k] + q[N - k])
print(ans)
