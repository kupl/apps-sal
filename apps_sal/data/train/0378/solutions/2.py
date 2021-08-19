class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort(reverse=True)
        print(nums)
        numsum = sum(nums)
        if numsum % 2 != 0:
            return False
        halfsum = numsum // 2
        t_sum = nums[0]
        if t_sum > halfsum:
            return False
        elif t_sum == halfsum:
            return True

        llen = len(nums)
        for startpos in range(1, llen):
            curpos = startpos
            while t_sum < halfsum and curpos < llen:
                if (t_sum + nums[curpos] > halfsum):
                    curpos += 1
                elif (t_sum + nums[curpos] == halfsum):
                    #print(curpos, t_sum,len(nums))
                    return True
                else:
                    t_sum += nums[curpos]
                    curpos += 1
                pass
            t_sum = nums[0]
        return False
