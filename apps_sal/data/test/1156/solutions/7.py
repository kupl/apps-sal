def run():
    n = int(input())
    a = [int(x) for x in input().split()]
    bt = [int(x) for x in input()]

    lmin = -(10**9)
    lmax = -lmin
    rmin = lmin
    rmax = lmax

    for i in range(4, n):
        prev = bt[i-1] + bt[i-2] + bt[i-3] + bt[i-4]
        if 0 < prev < 4:
            continue

        if prev == 0:

            acmp = max((a[i], a[i-1], a[i-2], a[i-3], a[i-4]))
            if bt[i] == 1:
                lminc = acmp + 1
                lmin = lminc if lminc > lmin else lmin
            else:
                lmaxc = acmp
                lmax = lmaxc if lmaxc < lmax else lmax

        elif prev == 4:

            acmp = min((a[i], a[i-1], a[i-2], a[i-3], a[i-4]))
            if bt[i] == 0:
                rmaxc = acmp - 1
                rmax = rmaxc if rmaxc < rmax else rmax
            else:
                rminc = acmp
                rmin = rminc if rminc > rmin else rmin

    print(f'{lmin} {rmax}')

run()
