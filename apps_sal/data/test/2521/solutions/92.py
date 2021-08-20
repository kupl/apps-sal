import heapq
N = int(input())
d = list(map(int, input().split()))
d_rev = d[::-1]
d1 = d[:N]
heapq.heapify(d1)
d2 = [-i for i in d_rev[:N]]
heapq.heapify(d2)
sum_d1 = sum(d1)
sum_d2 = sum(d2)
sum_d1_arr = [sum_d1]
sum_d2_arr = [sum_d2]
for k in range(N, 2 * N):
    c = sum_d1_arr[-1]
    c += d[k]
    n = heapq.heappushpop(d1, d[k])
    c -= n
    sum_d1_arr.append(c)
    e = sum_d2_arr[-1]
    e += -d_rev[k]
    n = heapq.heappushpop(d2, -1 * d_rev[k])
    e -= n
    sum_d2_arr.append(e)
print(max((v + w for (v, w) in zip(sum_d1_arr, sum_d2_arr[::-1]))))
