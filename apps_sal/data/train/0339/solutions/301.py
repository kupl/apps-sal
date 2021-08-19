class Solution:

    def numTriplets(self, nums1, nums2):
        res = 0
        for n in nums1:
            res += self.twoProduct(n * n, nums2)
        for n in nums2:
            res += self.twoProduct(n * n, nums1)
        return res

    def twoProduct(self, target, nums):
        count = 0
        compFreq = {}
        for i in range(len(nums)):
            comp = target / nums[i]
            if comp == int(comp):
                if nums[i] in compFreq:
                    count += compFreq[nums[i]]
                if comp in compFreq:
                    compFreq[comp] += 1
                else:
                    compFreq[comp] = 1
        return count
    '\n    # O(N^2) Solution\n    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int: \n        res = 0\n        \n        # freq is dict that has key=n^2, element=frequency of n^2 occur\n        # if there are duplicate in nums1=[2,2], and nums2=[1,4], there are 2 cases in stead on 1\n        freq1 = {}\n        freq2 = {}\n        for n in nums1:\n            if n*n in freq1:\n                freq1[n*n] += 1\n            else:\n                freq1[n*n] = 1\n        for n in nums2:\n            if n*n in freq2:\n                freq2[n*n] += 1\n            else:\n                freq2[n*n] = 1\n        \n        for b in range(len(nums2)-1):\n            for c in range(b+1, len(nums2)):\n                if (nums2[b] * nums2[c]) in freq1:\n                    res += freq1[nums2[b] * nums2[c]]\n                    \n        for b in range(len(nums1)-1):\n            for c in range(b+1, len(nums1)):\n                if (nums1[b] * nums1[c]) in freq2:\n                    res += freq2[nums1[b] * nums1[c]]\n        return res\n    '
