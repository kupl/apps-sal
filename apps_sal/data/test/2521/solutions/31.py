from collections import deque
from heapq import heapify, heappop, heappush
N = int(input())
tmp = list(map(int, input().split(' ')))
former_A = deque(tmp)
latter_A = deque(tmp.copy())
former_heap = list()
latter_heap = list()
for _ in range(N):
    former_heap.append(former_A.popleft())
    latter_heap.append(-latter_A.pop())
heapify(former_heap)
heapify(latter_heap)
former_sum = sum(former_heap)
former_sum_list = [former_sum]
for k in range(N):
    new_a = former_A.popleft()
    heappush(former_heap, new_a)
    min_a = heappop(former_heap)
    former_sum += new_a - min_a
    former_sum_list.append(former_sum)
latter_sum = sum(latter_heap)
latter_sum_list = [latter_sum]
for k in range(N):
    new_a = -latter_A.pop()
    heappush(latter_heap, new_a)
    min_a = heappop(latter_heap)
    latter_sum += new_a - min_a
    latter_sum_list.append(latter_sum)
latter_sum_list.reverse()
answer = max([former + latter for (former, latter) in zip(former_sum_list, latter_sum_list)])
print(answer)
