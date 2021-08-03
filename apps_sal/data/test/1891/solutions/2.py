# -*- coding: utf-8 -*-
# @Time    : 2019/2/4 0:20
# @Author  : LunaFire
# @Email   : gilgemesh2012@gmail.com
# @File    : C. Creative Snap.py


def main():
    n, k, a, b = list(map(int, input().split()))
    pos = list(map(int, input().split()))
    pos.sort()

    def search(interval_left, interval_right, index_left, index_right):
        if interval_left == interval_right:
            if index_left > index_right:
                # print('Interval:', interval_left, interval_right)
                # print('ANS:', a)
                return a
            else:
                # print('Interval:', interval_left, interval_right)
                # print('ANS:', b * (index_right - index_left + 1))
                return b * (index_right - index_left + 1)
        if index_left > index_right:
            return a

        interval_mid = interval_left + (interval_right - interval_left) // 2
        # print('MID:', interval_mid)
        left, right = index_left, index_right
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
        # print('Interval:', interval_left, interval_right)
        # print('ANS', ans)
        return min(t0, t1 + t2)

    ret = search(1, 1 << n, 0, k - 1)
    print(ret)


def __starting_point():
    main()


__starting_point()
