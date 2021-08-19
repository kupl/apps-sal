# -*- coding: utf-8 -*-
import heapq

N, Q = list(map(int, input().rstrip().split()))
AB_list = [list(map(int, input().rstrip().split())) for i in range(N)]
CD_list = [list(map(int, input().rstrip().split())) for i in range(Q)]
# -----

K = [[] for _ in range(2 * 10**5)]  # kindergarten
K_deleted = [[] for _ in range(2 * 10**5)]

max_K = []
max_K_deleted = []


for a, b in AB_list:
    heapq.heappush(K[b - 1], -a)

for member in K:
    if member:
        heapq.heappush(max_K, -member[0])


for c, d in CD_list:
    c_rate = AB_list[c - 1][0]
    c_prev = AB_list[c - 1][1]

    departure_prev_max = K[c_prev - 1][0]

    if K[d - 1]:
        destination_prev_max = K[d - 1][0]
    else:
        destination_prev_max = None

    # Delete c from current position
    heapq.heappush(K_deleted[c_prev - 1], -c_rate)

    # Add c to Destination(next position)
    AB_list[c - 1][1] = d
    heapq.heappush(K[d - 1], -c_rate)

    # check HeapQueue of current and destination
    for i in [c_prev, d]:
        while K_deleted[i - 1] and (K[i - 1][0] == K_deleted[i - 1][0]):
            heapq.heappop(K[i - 1])
            heapq.heappop(K_deleted[i - 1])

    # check max-rank at departure.
    if (not K[c_prev - 1]):
        heapq.heappush(max_K_deleted, -departure_prev_max)

    elif departure_prev_max != K[c_prev - 1][0]:
        heapq.heappush(max_K_deleted, -departure_prev_max)
        heapq.heappush(max_K, -K[c_prev - 1][0])

    # check max-rank at destination.
    if destination_prev_max != K[d - 1][0]:
        if destination_prev_max:
            heapq.heappush(max_K_deleted, -destination_prev_max)

        heapq.heappush(max_K, -K[d - 1][0])

    # check min-value among kindergarten
    while max_K_deleted and (max_K[0] == max_K_deleted[0]):
        heapq.heappop(max_K)
        heapq.heappop(max_K_deleted)

    print((max_K[0]))
