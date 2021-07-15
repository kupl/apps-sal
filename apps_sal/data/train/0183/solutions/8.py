class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        
        cache = {}
        
        def process(i, j, k):
            if not (i, j, k) in cache:
                ans = 0
                if i == 0 and j == 0:
                    if k == 0:
                        ans = nums1[i] * nums2[j]
                    else:
                        ans = max(nums1[i] * nums2[j], 0)
                elif i == 0:
                    ans = max(nums1[i] * nums2[j], process(i, j-1, k))
                elif j == 0:
                    ans = max(nums1[i] * nums2[j], process(i-1, j, k))
                else:
                    ans = max(nums1[i] * nums2[j] + process(i-1, j-1, 1), process(i-1, j, k), process(i, j-1, k))
                cache[(i, j, k)] = ans
            return cache[(i, j, k)]
            
        return process(n1-1, n2-1, 0)
