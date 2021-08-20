def main():
    import bisect
    import numpy as np
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    l1 = np.array(l)

    def bise(x):
        y = np.searchsorted(l1, x - l1)
        return n * n - y.sum()
    left = -1
    right = l[-1] * 2 + 1
    while right > left + 1:
        mid = (right + left) // 2
        if bise(mid) >= k:
            left = mid
        else:
            right = mid
    ans = 0
    count = 0
    acc = [0]
    for i in l:
        acc.append(acc[-1] + i)
    for i in l:
        index = bisect.bisect_left(l, right - i)
        ans += i * (n - index) + acc[n] - acc[index]
        count += n - index
    print(ans - (count - k) * left)


def __starting_point():
    main()


__starting_point()
