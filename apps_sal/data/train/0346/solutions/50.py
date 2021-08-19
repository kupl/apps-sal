class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        idxes = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                idxes.append(i)
        if len(idxes) < k:
            return 0
        res = 0
        for i in range(k - 1, len(idxes)):
            l = -1 if i - k + 1 == 0 else idxes[i - k]
            r = len(nums) if i == len(idxes) - 1 else idxes[i + 1]
            res += (idxes[i - k + 1] - l) * (r - idxes[i])
        return res
