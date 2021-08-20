from heapq import heappop, heappush
import sys
input = sys.stdin.readline
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
inf = 10 ** 12
left = [inf]
left_sum = 0
right = [inf]
right_sum = 0
cnt = 0
b = 0
for i in range(q):
    if query[i][0] == 1:
        a = query[i][1]
        b += query[i][2]
        if cnt == 0:
            d = right[0]
            if a > d:
                heappush(left, -heappop(right))
                heappush(right, a)
                right_sum += a - d
                left_sum -= d
            else:
                heappush(left, -a)
                left_sum -= a
            cnt = 1
        else:
            c = -left[0]
            if a < c:
                heappush(right, -heappop(left))
                heappush(left, -a)
                right_sum += c
                left_sum += c - a
            else:
                heappush(right, a)
                right_sum += a
            cnt = 0
    else:
        x = -left[0]
        if cnt == 0:
            print(x, b + right_sum + left_sum)
        else:
            print(x, b + x + right_sum + left_sum)
