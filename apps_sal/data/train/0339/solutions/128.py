class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1: List[int], nums2: List[int]) -> int:
            res = 0
            counter = Counter(nums2)
            for n1 in nums1:
                sq = n1 * n1
                for n2 in nums2:
                    if sq % n2 == 0:
                        num = sq / n2
                        res += counter[num]
                        if n1 == n2:
                            res -= 1
            return res
        
        return int((helper(nums1, nums2) + helper(nums2, nums1)) / 2)

