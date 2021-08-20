class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        res = 0
        for i in range(n1):
            x = nums1[i] ** 2
            mp = defaultdict(int)
            for j in range(n2):
                if x % nums2[j] == 0:
                    y = x // nums2[j]
                    if y in mp:
                        res += mp[y]
                mp[nums2[j]] += 1
        for i in range(n2):
            x = nums2[i] ** 2
            mp = defaultdict(int)
            for j in range(n1):
                if x % nums1[j] == 0:
                    y = x // nums1[j]
                    if y in mp:
                        res += mp[y]
                mp[nums1[j]] += 1
        return res
