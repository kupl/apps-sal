class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        res = []
        start_key = 0

        while start_key != len(nums):
            if nums[start_key] == 1:
                res.append(start_key)

            start_key += 1
        zero = 0
        while zero < len(res) - 1:
            if res[zero + 1] - (res[zero] + 1) < k:
                return False
            zero += 1

        return True
