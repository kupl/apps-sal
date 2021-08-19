class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def get_sqs(nums):
            c = collections.Counter()
            for j in range(len(nums)):
                for k in range(j + 1, len(nums)):
                    c[nums[j] * nums[k]] += 1
            return c
        sq1s = get_sqs(nums1)
        sq2s = get_sqs(nums2)
        res = 0
        for n in nums1:
            res += sq2s[n * n]
        for n in nums2:
            res += sq1s[n * n]
        return res
