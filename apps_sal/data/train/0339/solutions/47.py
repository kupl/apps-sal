class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def twoProd(n1, n2):
            d = Counter()
            for i, a in enumerate(n1):
                for j in range(i+1, len(n1)):
                    d[a*n1[j]] += 1
        
            return sum(d[i*i] for i in n2)
        
        return twoProd(nums1, nums2) + twoProd(nums2, nums1)        
