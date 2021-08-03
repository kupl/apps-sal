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

# L と r の選び方の組み合わせ数。1 から N までの和に等しい
lr_size = (N + 1) * N / 2


def count_lr(x):
    """
    x 以上の数を半分以上含む == 中央値が x 以上である、L と r の選び方の数
    :param x:
    :return:
    """
    ret = 0
    # series[i] が x 未満なら 1、x 以上なら -1 を i番目に持つ配列の、i=0 から i までの累積和。
    cumsum = 0
    # counts[i]: cumsum が i に何回なったか
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


# count_lr(x) の結果が半分以上であれば、中央値は x 以上。
# count_lr(x) が半分以上のうち一番大きい x を探す。
def solve(i):
    if count_lr(series_sorted[i]) >= (lr_size + 1) // 2:
        return 0
    else:
        return float('inf')


ans_i = bisect_right_callable(solve, 0, lo=0, hi=N)
print((series_sorted[max(0, min(N - 1, ans_i - 1))]))
