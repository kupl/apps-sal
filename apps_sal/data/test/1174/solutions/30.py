import heapq
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
a = list([x * (-1) for x in A])  # 各要素を-1倍

heapq.heapify(a)
for i in range(K):
    num = heapq.heappop(a) * (-1)
    heapq.heappush(a, -1 * (int(num / 2)))
    # print(num,a)
    if num == 0:
        break
print((-sum(a)))
