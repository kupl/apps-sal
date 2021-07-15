class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)    
        def dp(idx1, idx2, top: bool):
            
            if top:
                if idx1 < len(nums1):
                    while idx2 < len(nums2) and nums2[idx2] < nums1[idx1]:
                        idx2 += 1
                    if idx2 >= len(nums2):
                        return sum(nums1[idx1:])
                    if nums1[idx1] == nums2[idx2]:
                        return nums1[idx1] + max(dp(idx1+1, idx2+1, True), dp(idx1+1, idx2+1, False))
                    else:
                        return nums1[idx1] + dp(idx1+1, idx2, True)
                else:
                    return sum(nums1[idx1:])
            else:
                if idx2 < len(nums2):
                    while idx1 < len(nums1) and nums1[idx1] < nums2[idx2]:
                        idx1 += 1
                    if idx1 >= len(nums1):
                        return sum(nums2[idx2:])
                    if nums1[idx1] == nums2[idx2]:
                        return nums2[idx2] + max(dp(idx1+1, idx2+1, True), dp(idx1+1, idx2+1, False))
                    else:
                        return nums2[idx2] + dp(idx1, idx2+1, False)
                else:
                    return sum(nums2[idx2:])
                    
        return max(dp(0,0,True), dp(0,0,False)) % (10**9 + 7)
