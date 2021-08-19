import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x) * (-1), input().split()))
heapq.heapify(a)  # aを優先度付きキューに

for _ in range(m):
    tmp_min = heapq.heappop(a)
    heapq.heappush(a, (-1) * (-tmp_min // 2))  # 負数の剰余演算を避けるため一時的に0以上の整数にしています
print(-sum(a))
