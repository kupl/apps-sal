class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        triplets = 0
        
        for lst1, lst2 in (nums1, nums2), (nums2, nums1):
            for square in (n ** 2 for n in lst1):
                seen = defaultdict(int)
                for n in lst2:
                    if square % n == 0:
                        triplets += seen[square // n]
                    seen[n] += 1
                        
        return triplets
        

