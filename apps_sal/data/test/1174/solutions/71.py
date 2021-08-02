import heapq as hp
N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [-a for a in A]
hp.heapify(A)
for _ in range(M):
    x = hp.heappop(A)
    hp.heappush(A, x / 2)
A = [int(-a) for a in A]
print((sum(A)))
