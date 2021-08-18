import math


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        maxn = 0
        res = 0
        for i in range(len(nums)):
            if(nums[i] > 0):
                if(nums[i] > 0):
                    count = 0
                    n = nums[i]
                    while(n > 0):
                        if(n % 2 > 0):
                            res += 1
                            n = n - 1
                        else:
                            count += 1
                            n = n // 2
                    if(count > maxn):
                        maxn = count
        return(res + maxn)
