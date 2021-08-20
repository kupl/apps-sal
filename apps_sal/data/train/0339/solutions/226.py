class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        if len(nums1) == 1 and len(nums2) == 1:
            return 0
        if set(nums1) == set(nums2) and len(set(nums1)) == 1:
            res = len(nums2) * (len(nums2) - 1) // 2
            res = res * len(nums1)
            res = res + len(nums1) * (len(nums1) - 1) // 2 * len(nums2)
            return res
        m1 = self.getmultiply(nums1)
        m2 = self.getmultiply(nums2)
        for x in nums1:
            if x * x in m2:
                res = res + len(m2[x * x])
        for y in nums2:
            if y * y in m1:
                res = res + len(m1[y * y])
        return res

    def getmultiply(self, nums):
        res = {}
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] * nums[y] in res and [x, y]:
                    res[nums[x] * nums[y]].append([x, y])
                else:
                    res[nums[x] * nums[y]] = [[x, y]]
        return res

    def getsq(self, nums):
        res = {}
        for x in range(len(nums)):
            if nums[x] * nums[x] in res:
                if x not in res[nums[x] * nums[x]]:
                    res[nums[x] * nums[x]].append(x)
            else:
                res[nums[x] * nums[x]] = [x]
        return res
