class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        def helper(a, b):
            count = Counter(x ** 2 for x in a)
            return sum(count[x * y] for x, y in itertools.combinations(b, 2))

        return helper(nums1, nums2) + helper(nums2, nums1)
