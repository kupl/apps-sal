class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        pre = [0]
        for c in nums:
            pre.append(pre[-1] + c)
        res = 0
        dic = {}
        for c in pre:
            if c - k in dic:
                res += dic[c - k]
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1
        return res
