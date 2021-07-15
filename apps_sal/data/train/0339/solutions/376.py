class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums, lookup):
            # print('nums = {0}, lookup = {1}'.format(nums, lookup))
            res = 0
            for maxNum in nums:
                prod = maxNum * maxNum
                # print('maxNum = {0}, prod = {1}'.format(maxNum, prod))
                for n in lookup.keys():
                    if n <= maxNum and not prod % n:
                        m = prod // n
                        # print('m = {0}, n = {1}'.format(m, n))
                        
                        res += (lookup[n] * (lookup[n] - 1)) // 2 if m == n else lookup[m] * lookup[n]
            return res
        return helper(nums1, collections.Counter(nums2)) + helper(nums2, collections.Counter(nums1))
    
        
    # slown
    def numTriplets1(self, nums1: List[int], nums2: List[int]) -> int:
        lookup1, lookup2 = collections.defaultdict(int), collections.defaultdict(int)
        for n in nums1:
            lookup1[n] += 1
        for n in nums2:
            lookup2[n] += 1
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
