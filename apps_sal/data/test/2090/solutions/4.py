import sys
import heapq


def input():
    return sys.stdin.readline()


(n, k) = list(map(int, input().split()))
arr = [(0, 0)] * n
for i in range(n):
    (t, b) = list(map(int, input().split()))
    arr[i] = (t, b)
arr.sort(key=lambda x: (-x[1], -x[0]))
sum_length = 0
heap_length = []
for i in range(k):
    sum_length += arr[i][0]
    heapq.heappush(heap_length, arr[i][0])
min_beauty = arr[k - 1][1]
answer = sum_length * min_beauty
for i in range(k, n):
    min_beauty = arr[i][1]
    min_length = heapq.heappop(heap_length)
    temp = arr[i][0] - min_length
    if temp > 0:
        sum_length += temp
        heapq.heappush(heap_length, arr[i][0])
    else:
        heapq.heappush(heap_length, min_length)
    answer = max(answer, sum_length * min_beauty)
sum_length = 0
for i in range(k):
    sum_length += arr[i][0]
    min_beauty = arr[i][1]
    answer = max(answer, sum_length * min_beauty)
print(answer)
