import heapq
import collections
cnt = 1
cnts = collections.defaultdict(int)
median = 0
left_cnt = 0
right_cnt = 0
left_sum = 0
right_sum = 0
left_pos = []
right_pos = []
b = 0
q = int(input())
initial = list(map(int, input().split()))
median = initial[1]
b += initial[2]
cnts[median] = 1
for _ in range(q - 1):
    query = list(map(int, input().split()))
    if query[0] == 1:
        cnt += 1
        b += query[2]
        if query[1] == median:
            cnts[median] += 1
        elif query[1] < median:
            left_cnt += 1
            left_sum += query[1]
            cnts[query[1]] += 1
            if cnts[query[1]] == 1:
                heapq.heappush(left_pos, -query[1])
        elif query[1] > median:
            right_cnt += 1
            right_sum += query[1]
            cnts[query[1]] += 1
            if cnts[query[1]] == 1:
                heapq.heappush(right_pos, query[1])
        if left_cnt + 1 <= (cnt + 1) // 2 <= left_cnt + cnts[median]:
            continue
        elif left_cnt + 1 > (cnt + 1) // 2:
            heapq.heappush(right_pos, median)
            right_cnt += cnts[median]
            right_sum += median * cnts[median]
            median = -heapq.heappop(left_pos)
            left_cnt -= cnts[median]
            left_sum -= median * cnts[median]
        elif (cnt + 1) // 2 > left_cnt + cnts[median]:
            heapq.heappush(left_pos, -median)
            left_cnt += cnts[median]
            left_sum += median * cnts[median]
            median = heapq.heappop(right_pos)
            right_cnt -= cnts[median]
            right_sum -= median * cnts[median]
    elif query[0] == 2:
        value = b
        if left_cnt != 0:
            value += abs(left_sum - median * left_cnt)
        if right_cnt != 0:
            value += abs(right_sum - median * right_cnt)
        print(median, value)
