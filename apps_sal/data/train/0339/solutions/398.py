class Solution:

    def work(self, nums1, nums2):
        res = 0
        dic = {}
        for num in nums1:
            if num * num in dic:
                dic[num * num] += 1
            else:
                dic[num * num] = 1

        n = len(nums2)
        for i in range(n):
            for j in range(i + 1, n):
                if nums2[i] * nums2[j] in dic:
                    res += dic[nums2[i] * nums2[j]]
        return res

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.work(nums1, nums2) + self.work(nums2, nums1)
