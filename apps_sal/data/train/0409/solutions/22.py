class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if not arr or k == 0:
            return 0
        max_sub_arr, total = self.get_max_subarr(arr, 0, len(arr))
        res = 0
        l = self.get_left_max(arr)
        r = self.get_right_max(arr)
        if k == 1:
            return max_sub_arr
        pos = 0
        if k > 3:
            pos = (l + r) + (k - 2) * total

        return max(total * k, max_sub_arr, (l + r), pos) % (10**9 + 7)

    def get_right_max(self, arr):
        res = 0
        cur = 0
        i = len(arr) - 1
        while i >= 0:
            cur += arr[i]
            res = max(cur, res)
            i -= 1
        return res

    def get_left_max(self, arr):
        res = 0
        cur = 0
        i = 0
        while i < len(arr):
            cur += arr[i]
            res = max(cur, res)
            i += 1
        return res

    def get_max_subarr(self, nums, i, j):
        cur = 0
        res = 0
        total = 0
        for it in range(i, j):
            total += nums[it]
            if nums[it] >= 0:
                cur += nums[it]
                res = max(cur, res)
            else:
                cur = max(cur + nums[it], 0)
        return res, total
