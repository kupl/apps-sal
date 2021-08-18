def bisect_right_callable(fn, x, lo, hi):
    """
    lo から hi-1 のうち、fn の結果が x 以下となる、最も右の値 + 1
    bisect.bisect_right と同じ
    https://docs.python.org/ja/3/library/bisect.html
    :param callable fn:
    :param x:
    :param int lo: 最小値
    :param int hi: 最大値 + 1
    :return: lo <= ret <= hi
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if x < fn(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


N = int(input())
series = list(map(int, input().split()))
series_sorted = sorted(series)

lr_size = (N + 1) * N / 2


def count_lr(x):
    """
    x 以上の数を半分以上含む == 中央値が x 以上である、L と r の選び方の数
    :param x:
    :return:
    """
    ret = 0
    cumsum = 0
    counts = {i: 0 for i in range(-N, N + 1)}
    counts[cumsum] = 1
    diff = 0
    for i in range(N):
        if series[i] >= x:
            cumsum += 1
            counts[cumsum] += 1
            diff += counts[cumsum]
        else:
            cumsum -= 1
            counts[cumsum] += 1
            diff -= counts[cumsum + 1] - 1
        ret += diff
    return ret


def solve(i):
    if count_lr(series_sorted[i]) >= (lr_size + 1) // 2:
        return 0
    else:
        return float('inf')


ans_i = bisect_right_callable(solve, 0, lo=0, hi=N)
print((series_sorted[max(0, min(N - 1, ans_i - 1))]))
