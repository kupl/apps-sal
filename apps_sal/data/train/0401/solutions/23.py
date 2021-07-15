class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l0 = [i for i in nums if i % 3 == 0]
        l1 = [i for i in nums if i % 3 == 1]
        l2 = [i for i in nums if i % 3 == 2]
        
        print((l0, l1, l2))
        
        total_sum = sum(nums)
        
        res = total_sum
        
        if total_sum % 3 != 0:
            
            if total_sum % 3 == 1:
                res1 = sum(l0) + sum(l1[1:]) + sum(l2)
                res2 = sum(l0) + sum(l1) + sum(l2[2:])

            elif total_sum % 3 == 2:
                res1 = sum(l0) + sum(l1[2:]) + sum(l2)
                res2 = sum(l0) + sum(l1) + sum(l2[1:])
            
            if res1 % 3 == 0 and res2%3 == 0:
                res = max(res1, res2)
            elif res1 % 3 == 0:
                res = res1
            else:
                res = res2
        
        return res

