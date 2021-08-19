class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import defaultdict
        import math
        n = len(nums1)
        m = len(nums2)
        dic1, dic2 = defaultdict(int), defaultdict(int)
        for i in range(n):
            dic1[nums1[i]] += 1
        for i in range(m):
            dic2[nums2[i]] += 1
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                x = nums1[i] * nums1[j]
                y = math.sqrt(x)
                if y % 1 == 0:
                    # print(y,'y','nunms1',i,j)
                    ans += dic2[y]
        for i in range(m):
            for j in range(i + 1, m):
                x = nums2[i] * nums2[j]
                y = math.sqrt(x)
                if y % 1 == 0:
                    # print(y,'y','nunms2')
                    ans += dic1[y]
        return ans
