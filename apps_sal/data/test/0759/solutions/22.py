from math import ceil
(hh, mm) = list(map(int, input().split()))
(H, D, C, N) = list(map(int, input().split()))
time_now = 60 * hh + mm
time_sale = 60 * 20
d_time = time_sale - time_now
c = 0.8 * C
if d_time <= 0:
    print('{:.4f}'.format(ceil(H / N) * c))
else:
    print('{:.4f}'.format(min(ceil(H / N) * C, ceil((H + D * d_time) / N) * c)))
