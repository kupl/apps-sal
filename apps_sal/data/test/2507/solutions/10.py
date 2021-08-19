import numpy as np


def main():
    (N, K) = [int(x) for x in input().split()]
    A = [float(x) for x in input().split()]
    F = [float(x) for x in input().split()]
    A = np.array(sorted(A))
    F = np.array(sorted(F, reverse=True))
    if K >= np.sum(A) * N:
        print(0)
        return
    min_time = 0
    max_time = A[-1] * F[0]
    while max_time != min_time:
        tgt_time = (min_time + max_time) // 2
        ideal_a = np.floor(tgt_time * np.ones(N) / F)
        cost = A - ideal_a
        require_k = np.sum(cost[cost > 0])
        if require_k <= K:
            max_time = tgt_time
        else:
            min_time = tgt_time + 1
    print(int(max_time))


def __starting_point():
    main()


__starting_point()
