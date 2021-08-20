def main():
    (n, k, a, b) = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    pos.sort()

    def search(interval_left, interval_right, index_left, index_right):
        if interval_left == interval_right:
            if index_left > index_right:
                return a
            else:
                return b * (index_right - index_left + 1)
        if index_left > index_right:
            return a
        interval_mid = interval_left + (interval_right - interval_left) // 2
        (left, right) = (index_left, index_right)
        index_mid = left - 1
        while left <= right:
            mid = (left + right) // 2
            if pos[mid] <= interval_mid:
                index_mid = mid
                left = left + 1
            else:
                right = right - 1
        t0 = b * (index_right - index_left + 1) * (interval_right - interval_left + 1)
        t1 = search(interval_left, interval_mid, index_left, index_mid)
        t2 = search(interval_mid + 1, interval_right, index_mid + 1, index_right)
        ans = min(t0, t1 + t2)
        return min(t0, t1 + t2)
    ret = search(1, 1 << n, 0, k - 1)
    print(ret)


def __starting_point():
    main()


__starting_point()
