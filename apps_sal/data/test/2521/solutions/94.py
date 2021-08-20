from heapq import heappush, heappop
n = int(input())
a = list(map(int, input().split()))
max_sum_fh = [0] * (n + 1)
min_sum_lh = [0] * (n + 1)
hq_fh = []
hq_lh = []
for i in range(n):
    heappush(hq_fh, a[i])
    heappush(hq_lh, -a[-1 - i])
max_sum_fh[0] = sum(hq_fh)
min_sum_lh[n] = -sum(hq_lh)
for i in range(n):
    if a[i + n] > hq_fh[0]:
        value_in = a[i + n]
        value_out = heappop(hq_fh)
        heappush(hq_fh, value_in)
        max_sum_fh[i + 1] = max_sum_fh[i] - value_out + value_in
    else:
        max_sum_fh[i + 1] = max_sum_fh[i]
    if -a[-1 - i - n] > hq_lh[0]:
        value_in = -a[-1 - i - n]
        value_out = heappop(hq_lh)
        heappush(hq_lh, value_in)
        min_sum_lh[-2 - i] = min_sum_lh[-1 - i] + value_out - value_in
    else:
        min_sum_lh[-2 - i] = min_sum_lh[-1 - i]
print(max([max_sum_fh[i] - min_sum_lh[i] for i in range(n + 1)]))
