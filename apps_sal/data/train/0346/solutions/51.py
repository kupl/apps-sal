class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = {0: 1}
        count = 0
        nice = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1
            if count - k in dic:
                nice += dic[count - k]
            dic[count] = dic.get(count, 0) + 1
        return nice
