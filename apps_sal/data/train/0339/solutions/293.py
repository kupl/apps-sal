class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (memo1, memo2) = (collections.Counter(), collections.Counter())
        for (a, b) in itertools.combinations(nums1, 2):
            temp = int(math.sqrt(a * b))
            if temp ** 2 == a * b:
                memo1[temp] += 1
        for (a, b) in itertools.combinations(nums2, 2):
            temp = int(math.sqrt(a * b))
            if temp ** 2 == a * b:
                memo2[temp] += 1
        return sum((memo2[num] for num in nums1)) + sum((memo1[num] for num in nums2))
