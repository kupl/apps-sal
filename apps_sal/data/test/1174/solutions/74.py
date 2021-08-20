from heapq import heapify, heappop, heappush
(N, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
q = []
for a in A:
    q.append((a // 2 - a, a, 1))
heapify(q)
ans = sum(A)
for _ in range(M):
    (discount, a, n) = heappop(q)
    ans += discount
    if ans == 0:
        break
    heappush(q, (a // 2 ** (n + 1) - a // 2 ** n, a, n + 1))
print(ans)
