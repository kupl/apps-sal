import sys
readline = sys.stdin.readline


def main():
    (N, C) = map(int, readline().rstrip().split())
    pair = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    x_acc_right = []
    (gain, max_gain) = (0, 0)
    for (xi, vi) in pair:
        gain += vi
        max_gain = max(max_gain, gain - xi)
        x_acc_right.append(max_gain)
    x_acc_left = []
    (gain, max_gain) = (0, 0)
    for (xi, vi) in pair[::-1]:
        gain += vi
        max_gain = max(max_gain, gain - (C - xi))
        x_acc_left.append(max_gain)
    res = max(x_acc_right[-1], x_acc_left[-1])
    gain = 0
    for i in range(N - 1):
        (xi, vi) = pair[i]
        gain += vi
        res = max(res, gain - 2 * xi + x_acc_left[N - i - 2])
    gain = 0
    for i in range(N - 1, 0, -1):
        (xi, vi) = pair[i]
        gain += vi
        res = max(res, gain - 2 * (C - xi) + x_acc_right[i - 1])
    print(res)


def __starting_point():
    main()


__starting_point()
