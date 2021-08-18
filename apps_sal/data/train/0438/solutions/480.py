from bisect import bisect_left


class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        n = len(arr)
        segments = [(1, n)]
        if m == n:
            return n
        for cur_iter, zero in enumerate(arr[::-1]):
            index = bisect_left(segments, (zero, 9999999999)) - 1
            seg = segments[index]
            if seg[1] == 1 and seg[0] == zero:
                del segments[index]
            elif seg[1] == 1:
                assert False
            else:
                del segments[index]
                first_length = zero - seg[0]
                second_length = seg[0] + seg[1] - 1 - zero
                if first_length == m or second_length == m:
                    return n - cur_iter - 1
                if second_length >= 1:
                    segments.insert(index, (zero + 1, second_length))
                if first_length >= 1:
                    segments.insert(index, (seg[0], first_length))
        return -1
