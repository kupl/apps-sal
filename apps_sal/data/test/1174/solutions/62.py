import heapq
N, M = list(map(int, input().split()))
A = list([int(x) * (-1) for x in input().split()])  # 各要素を-1倍
heapq.heapify(A)  # Aを優先度付きキューに

for _ in range(M):
    temp_min = heapq.heappop(A)
    heapq.heappush(A, (-1) * (temp_min * (-1) // 2))
print((-sum(A)))
