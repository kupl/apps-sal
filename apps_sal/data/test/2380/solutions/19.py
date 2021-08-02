import heapq

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

heapq.heapify(A)

BC = [list(map(int, input().split())) for j in range(M)]
BC.sort(key=lambda x: x[1], reverse=True)

for i in range(M):
    B, C = BC[i]
    for j in range(B):
        num = heapq.heappop(A)
        if num < C:
            heapq.heappush(A, C)
        else:
            heapq.heappush(A, num)
            break

print((sum(A)))
