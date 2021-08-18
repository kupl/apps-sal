from heapq import heapify, heappush, heappop
import sys
input = sys.stdin.readline

Q = int(input())
querys = [tuple(map(int, input().split())) for _ in range(Q)]

anss = []
PQL, PQR = [], []
sumL = sumR = 0
numL = numR = 0
sumB = 0
for query in querys:
    if query[0] == 1:
        a, b = query[1:]
        sumB += b
        if numL == 0:
            heappush(PQL, -a)
            sumL += a
            numL += 1
        elif numL == numR:
            if a <= -PQL[0]:
                heappush(PQL, -a)
                sumL += a
                numL += 1
            else:
                heappush(PQR, a)
                c = heappop(PQR)
                sumR += a - c
                heappush(PQL, -c)
                sumL += c
                numL += 1
        else:
            if a < -PQL[0]:
                heappush(PQL, -a)
                c = -heappop(PQL)
                sumL += a - c
                heappush(PQR, c)
                sumR += c
                numR += 1
            else:
                heappush(PQR, a)
                sumR += a
                numR += 1

    else:
        x = -PQL[0]
        fx = numL * x - sumL + sumR - numR * x + sumB
        anss.append((x, fx))

print(('\n'.join([str(x[0]) + ' ' + str(x[1]) for x in anss])))
