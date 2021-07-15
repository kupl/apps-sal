from collections import defaultdict
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        def helper(nums1, nums2):
            ans = 0
            for num1 in nums1:
                exist = defaultdict(int)
                v = num1 * num1
                for num2 in nums2:
                    if v % num2 == 0 and v / num2 in exist:
                        ans += exist[v / num2]
                    exist[num2] += 1
                    
            return ans
        return helper(nums1, nums2) + helper(nums2, nums1)
                

