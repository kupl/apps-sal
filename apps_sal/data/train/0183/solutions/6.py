class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def cal(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0
            
            return max(nums1[i]*nums2[j] + cal(i+1, j+1), cal(i, j+1), cal(i+1, j))
        
        ans =  cal(0, 0)
        if ans == 0:
            return max(min(nums1)*max(nums2), min(nums2)*max(nums1))
        else:
            return ans
