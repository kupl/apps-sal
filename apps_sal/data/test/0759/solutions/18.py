from math import ceil
h, m = list(map(int, input().split()))
H, D, C, N = list(map(int, input().split()))
if h >= 20:
    print(0.8 * C * ceil(H / N))
else:
    minutes = 20 * 60 - h * 60 - m
    no_wait = C * ceil(H / N)
    with_wait = 0.8 * C * ceil((H + D * minutes) / N)
    print(min(with_wait, no_wait))

