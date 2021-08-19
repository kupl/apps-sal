class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        idx = [n for (n, x) in enumerate(nums) if x == 1]
        for i in range(1, len(idx)):
            print((idx[i], idx[i - 1]))
            if idx[i] - idx[i - 1] <= k:
                return False
        return True
