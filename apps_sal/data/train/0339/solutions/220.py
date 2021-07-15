from itertools import combinations

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def isPerSq(n):
            return int(math.sqrt(n) + 0.5) ** 2 == n
        
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        
        s = 0
        for x,y in combinations(nums2, 2):
            if isPerSq(x*y):
                s += d1[math.sqrt(x*y)]
        
        for x,y in combinations(nums1, 2):
            if isPerSq(x*y):
                s += d2[math.sqrt(x*y)]
        
        return s
