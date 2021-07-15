class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(n1, n2):
            ret = 0
            for x in n1:
                seen = collections.defaultdict(int)
                for y in n2:
                    if x*x % y == 0:
                        ret += seen[x*x // y]
                    seen[y] += 1    
            return ret
        return count(nums1, nums2) + count(nums2, nums1)
