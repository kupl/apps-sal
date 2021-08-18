import sys
from itertools import accumulate


def main():
    n, k, q = list(map(int, sys.stdin.readline().split()))
    ary = [0] * 2000001
    num_valid = [0] * 2000001
    max_temp = -1
    for __ in range(n):
        s, t = list(map(int, sys.stdin.readline().split()))
        ary[s - 1] += 1
        ary[t] -= 1

    tot = 0
    for indx in range(len(num_valid) - 1):
        tot += ary[indx]
        num_valid[indx + 1] = num_valid[indx] + (tot >= k)

    for __ in range(q):
        s, t = list(map(int, sys.stdin.readline().split()))
        print(num_valid[t] - num_valid[s - 1])


def __starting_point():
    main()


__starting_point()
