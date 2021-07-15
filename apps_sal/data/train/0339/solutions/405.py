class Solution:
    def numTriplets(self, f: List[int], s: List[int]) -> int:
        from collections import defaultdict
        
        
        def helper(nums1, nums2):
            d = defaultdict(int)
            ans = 0    

            for i in range(len(nums1)):
                for j in range(i+1, len(nums1)):
                    d[nums1[i]* nums1[j]]+= 1

            for num in nums2:
                ans += d[num**2]
            return ans
                
        return helper(f,s )+ helper(s,f)
