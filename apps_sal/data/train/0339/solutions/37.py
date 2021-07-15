class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from math import sqrt
        from collections import Counter
        def find(target, pool):
            ans = 0
            target = Counter(target)
            for i in range(0, len(pool)-1):
                for j in range(i + 1, len(pool)):
                    ans += target.get(sqrt(pool[i]*pool[j]), 0)
            return ans
        
        return find(nums1, nums2) + find(nums2, nums1)
