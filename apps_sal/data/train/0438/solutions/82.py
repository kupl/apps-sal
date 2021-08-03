class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        res = -1
        if n == m:
            return n
        set_range = [0] * (n + 2)
        for i in range(n):
            set_bit = arr[i]
            left_range = set_range[set_bit - 1]
            right_range = set_range[set_bit + 1]
            set_range[set_bit] = left_range + right_range + 1
            set_range[set_bit - left_range] = set_range[set_bit + right_range] = set_range[set_bit]
            if left_range == m or right_range == m:
                res = i

        return res
