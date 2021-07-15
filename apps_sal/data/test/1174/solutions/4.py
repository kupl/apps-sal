import heapq

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_list_minus = list(map(lambda x: x*(-1), A_list))  # 各要素を-1倍
heapq.heapify(A_list_minus)

for i in range(M):
    tmp_max = heapq.heappop(A_list_minus)*(-1)
    heapq.heappush(A_list_minus, (-1)*(tmp_max//2)) #挿入するときは最小に

print(-1*sum(A_list_minus))
