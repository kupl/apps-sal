from heapq import heappop, heappush
(X, Y, Z, K) = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)
l = []
for a in A:
    for b in B:
        l.append(-a - b)
l.sort()
l = l[:K] if len(l) >= K else l + [0] * (K - len(l))
ans = []
for c in C:
    for i in l:
        heappush(ans, i - c)
for i in range(K):
    print(-heappop(ans))
