import heapq
import copy
N,K = map(int, input().split())
V_list= list(map(int, input().split()))

selected = []
left = []

max_sum = 0
left_sum = 0
for l in range(N):
    selected = copy.deepcopy(left)
    lr_sum = left_sum
    for r in range(N-l+1):
        # skip
        stock = K-l-r
        if stock < 0:
            break
        ri = N-r-1
        select_cnt = len(selected)
        tmp_sum = lr_sum
        max_sum = max(max_sum, tmp_sum)
        popper = copy.deepcopy(selected)

        for i in range(stock):
            if i >= select_cnt:
                break
            
            pop_v = heapq.heappop(popper)
            if pop_v > 0:
                break
            tmp_sum -= pop_v
            max_sum = max(max_sum, tmp_sum)

        r_val = V_list[ri]
        lr_sum += r_val
        heapq.heappush(selected, r_val)

    l_val = V_list[l]
    left_sum += l_val
    heapq.heappush(left, l_val)

print(max_sum)
