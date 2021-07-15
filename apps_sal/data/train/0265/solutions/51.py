class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        count = 0
        curr_cnt = 0
        dic = {0:-1}
        for i in range(len(nums)):
            curr_cnt += nums[i]
            if curr_cnt - target in dic:
                count += 1
                dic = {}
            dic[curr_cnt] = i
        return count
        

