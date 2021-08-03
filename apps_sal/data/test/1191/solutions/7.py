import heapq
n, k = list(map(int, input().split()))
p = list(map(int, input().split()))
c = list(map(int, input().split()))
indexes = sorted(list(range(n)), key=p.__getitem__)
most_vyg_odn_yye = []
res = [1] * n
cur_res = 0
for ind in indexes:
    this_cost = c[ind]
    heapq.heappush(most_vyg_odn_yye, this_cost)
    cur_res += this_cost
    res[ind] = cur_res
    if len(most_vyg_odn_yye) > k:
        cur_res -= heapq.heappop(most_vyg_odn_yye)
print(*res)
