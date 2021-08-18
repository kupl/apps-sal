
from heapq import heappush, heappop

t = 1

for test in range(t):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    heap = []
    ans = []
    cur_sum = 0
    for i in range(n):
        tmp_sum = cur_sum
        cur = 0
        popped = []
        while tmp_sum + arr[i] > m:
            val = heappop(heap)
            tmp_sum += val
            cur += 1
            popped.append(val)
        while popped:
            heappush(heap, popped.pop())

        cur_sum += arr[i]
        heappush(heap, -arr[i])
        ans.append(cur)
    print(*ans)
