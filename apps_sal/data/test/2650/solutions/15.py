import heapq

N, Q = map(int, input().split())

yochien = {}
rate = {}
enzi_rate = {}
enzi_rate_out = {}
result = []

for i in range(1, N + 1):
    A, B = map(int, input().split())

    rate[i] = A
    yochien[i] = B

    if B not in enzi_rate:
        enzi_rate[B] = []
    heapq.heappush(enzi_rate[B], -A)


max_enzi = []
heapq.heapify(max_enzi)
max_enzi_out = []
heapq.heapify(max_enzi_out)

for j in enzi_rate:
    heapq.heappush(max_enzi, -enzi_rate[j][0])

for _ in range(Q):
    C, D = map(int, input().split())

    if yochien[C] not in enzi_rate_out:
        enzi_rate_out[yochien[C]] = []
    heapq.heappush(enzi_rate_out[yochien[C]], -rate[C])

    if len(enzi_rate_out[yochien[C]]) >= 1 and enzi_rate_out[yochien[C]][0] == enzi_rate[yochien[C]][0]:
        heapq.heappush(max_enzi_out, -enzi_rate_out[yochien[C]][0])
        while len(enzi_rate_out[yochien[C]]) >= 1 and enzi_rate_out[yochien[C]][0] == enzi_rate[yochien[C]][0]:
            heapq.heappop(enzi_rate_out[yochien[C]])
            heapq.heappop(enzi_rate[yochien[C]])
        if len(enzi_rate[yochien[C]]) >= 1:
            heapq.heappush(max_enzi, -enzi_rate[yochien[C]][0])

    yochien[C] = D

    if D not in enzi_rate or len(enzi_rate[D]) == 0:
        enzi_rate[D] = []
        heapq.heappush(max_enzi, rate[C])
    elif -enzi_rate[D][0] < rate[C]:
        heapq.heappush(max_enzi, rate[C])
        heapq.heappush(max_enzi_out, -enzi_rate[D][0])

    heapq.heappush(enzi_rate[D], -rate[C])

    while len(max_enzi_out) >= 1 and max_enzi[0] == max_enzi_out[0]:
        heapq.heappop(max_enzi)
        heapq.heappop(max_enzi_out)

    result.append(max_enzi[0])

for k in range(Q):
    print(result[k])
