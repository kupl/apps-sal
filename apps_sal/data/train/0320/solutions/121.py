from math import log

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        vposes = set(range(len(nums)))
        while vposes:
            rm = set()
            for i in vposes:
                if nums[i] % 2:
                    nums[i] -= 1
                    res += 1
                if not nums[i]:
                    rm.add(i)
            vposes.symmetric_difference_update(rm)        
            chg = False
            for i in vposes:
                chg = True
                nums[i] //= 2
            res += chg    
        return res    

