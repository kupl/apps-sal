from bisect import bisect_left, bisect_right

n, x, k = [int(i) for i in input().split(' ')]
ar = sorted([int(i) for i in input().split(' ')])

lk, nk = -1, 0

n_tup = 0

if x != 1 or k != 0:
    for i in range(len(ar)):
        nk = ar[i]
        if lk != nk:
            xf = (k + (ar[i] - 1) // x)
            lo = bisect_left(ar, ar[i])
            # Find rightmost value less than xf*x
            lt = bisect_left(ar, (xf + 1) * x, lo)
            # Find leftmost value greater than (xf+1)*x
            gt = bisect_right(ar, xf * x - 1, lo)
        n_tup += lt - gt
        lk = nk

print(n_tup)
