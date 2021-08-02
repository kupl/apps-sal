# alpha = "abcdefghijklmnopqrstuvwxyz"
# prime = 998244353
# INF = 1000_000_000

from heapq import heappush, heappop
# from collections import defaultdict
# from math import sqrt
# from collections import deque

t = 1  # int(input())

for test in range(t):
    # n = int(input())
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
