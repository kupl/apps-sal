import sys
def input():return sys.stdin.readline().strip()
from collections import defaultdict
from heapq import heappop, heappush, heapify

def main():
    N, Q = map(int, input().split())
    infant_info = [tuple(map(int, input().split())) for _ in range(N)]
    queries = [tuple(map(int, input().split())) for _ in range(Q)]
    
    num_kd = 2 * 10 ** 5
    nums = [0] * num_kd
    h = [[] for _ in range(num_kd)]
    pos = [-1] * N
    kd_max = defaultdict(int)
    min_max_timestamp = [0] * num_kd

    # init
    for i, (a, b) in enumerate(infant_info):
        b -= 1

        heappush(h[b], (-a, i))
        pos[i] = b
        nums[b] += 1

        kd_max[b] = max(kd_max[b], a)
    
    # rate, id, timestamp
    min_max_h = [(val, kd, 0) for kd, val in kd_max.items()]

    heapify(min_max_h)

    # query
    for t, (c, to_kd) in enumerate(queries, 1):
        c -= 1
        to_kd -= 1

        from_kd = pos[c]
        pos[c] = to_kd

        # from
        nums[from_kd] -= 1
        if nums[from_kd] > 0:
            while True:
                rate, infant = heappop(h[from_kd])
                if pos[infant] == from_kd:
                    heappush(h[from_kd], (rate, infant))
                    heappush(min_max_h, (-rate, from_kd, t))
                    break
        
        min_max_timestamp[from_kd] = t

        
        # to
        nums[to_kd] += 1

        rate_c, _ = infant_info[c]
        heappush(h[to_kd], (-rate_c, c))

        while True:
            rate, infant = heappop(h[to_kd])
            if pos[infant] == to_kd:
                heappush(h[to_kd], (rate, infant))
                heappush(min_max_h, (-rate, to_kd, t))
                break
        
        min_max_timestamp[to_kd] = t



        # equality
        # print("pos", pos)
        while True:
            rate, kd, ts = heappop(min_max_h) 
            if min_max_timestamp[kd] == ts:
                print(rate)
                heappush(min_max_h, (rate, kd, ts))
                break
    
def __starting_point():
    main()
__starting_point()
