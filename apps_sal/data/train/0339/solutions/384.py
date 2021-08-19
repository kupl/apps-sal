class Solution:
    # https://leetcode.com/submissions/detail/404293310/
    # fast
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums, lookup):
            res = 0
            for maxNum in nums:
                prod = maxNum * maxNum
                for n in lookup.keys():
                    if n <= maxNum and not prod % n:
                        m = prod // n
                        # m ==n, combination.
                        res += (lookup[n] * (lookup[n] - 1)) // 2 if m == n else lookup[m] * lookup[n]
            return res
        return helper(nums1, collections.Counter(nums2)) + helper(nums2, collections.Counter(nums1))

    # slow

    def numTriplets1(self, nums1: List[int], nums2: List[int]) -> int:
        lookup1, lookup2 = collections.defaultdict(int), collections.defaultdict(int)
        lookup1, lookup2 = collections.Counter(nums1), collections.Counter(nums2)
        res = 0
        for k in [0, 1]:
            nums = nums1 if not k else nums2
            lookup = lookup1 if k else lookup2
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    prod = nums[i] * nums[j]
                    k = int(math.sqrt(prod))
                    if k * k == prod and k in lookup:
                        res += lookup[k]
        return res
