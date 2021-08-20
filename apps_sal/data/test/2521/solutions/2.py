import heapq as hq
from collections import defaultdict
import sys
readline = sys.stdin.readline
N = int(readline())
A = list(map(int, readline().split()))
sortA = sorted(A[:2 * N])
smallA = sortA[:N]
small_dic = defaultdict(int)
for i in range(len(smallA)):
    small_dic[smallA[i]] += 1
largeA = sortA[N:]
large_dic = defaultdict(int)
for i in range(len(largeA)):
    large_dic[largeA[i]] += 1
leftsum = sum(sortA[N:])
leftq = list([-x for x in smallA])
hq.heapify(leftq)
rightq = A[2 * N:]
rightsum = sum(rightq)
rightq = list([-x for x in rightq])
hq.heapify(rightq)
ans = leftsum - rightsum
for i in range(2 * N - 1, N - 1, -1):
    if large_dic[A[i]] > 0:
        large_dic[A[i]] -= 1
        leftsum -= A[i]
        while True:
            move = -hq.heappop(leftq)
            if small_dic[move] > 0:
                small_dic[move] -= 1
                break
        leftsum += move
        large_dic[move] += 1
    else:
        small_dic[A[i]] -= 1
    hq.heappush(rightq, -A[i])
    rem = -hq.heappop(rightq)
    rightsum += A[i]
    rightsum -= rem
    if ans < leftsum - rightsum:
        ans = leftsum - rightsum
print(ans)
