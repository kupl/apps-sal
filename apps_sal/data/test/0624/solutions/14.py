
import sys
import math


def main():
    fin = sys.stdin
    n, k, m = list(map(int, list(fin.readline().strip().split())))
    a = list(map(int, list(fin.readline().strip().split())))
    a = sorted(a, reverse=True)
    sm = sum(a)
    avg = sm / n
    maxavg = -math.inf
    dyn_sm = sm
    for n_rm in range(0, n):
        if n_rm > m:
            break
        dyn_sm -= a[n - n_rm] if n_rm > 0 else 0
        dyn_avg = (dyn_sm + ((n - n_rm) * k if (n - n_rm) * k <= m - n_rm else m - n_rm)) / (n - n_rm)
        maxavg = max(maxavg, dyn_avg)
    print(maxavg)


def __starting_point():
    main()


__starting_point()
