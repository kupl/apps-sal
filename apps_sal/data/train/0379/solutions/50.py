class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        l1 = []
        d = {}
        d1 = {}
        d2 = {}

        for i in nums1:
            d[i] = 1
        for i in nums2:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if d[i] == 2:
                l1.append(i)

        l1.sort()
        n1 = len(l1) + 1
        l1.insert(0, 0)

        dp = [[0 for j in range(2)] for i in range(n1 + 1)]
        pref1 = [0] * (len(nums1) + 1)
        pref2 = [0] * (len(nums2) + 1)

        for i in range(len(nums1)):
            d1[nums1[i]] = i
            pref1[i + 1] = pref1[i] + nums1[i]

        for i in range(len(nums2)):
            d2[nums2[i]] = i
            pref2[i + 1] = pref2[i] + nums2[i]
        # print(d1,d2)
        d1[0] = 0
        d2[0] = 0
        for i in range(1, n1):

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + pref1[d1[l1[i]] + 1] - pref1[d1[l1[i - 1]]] - l1[i - 1]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + pref2[d2[l1[i]] + 1] - pref2[d2[l1[i - 1]]] - l1[i - 1]
            # print(123,l1[i],dp[i][0],dp[i][1])
        # print(l1)
        return (max(dp[n1 - 1][0], dp[n1 - 1][1]) + max(pref1[len(nums1)] - pref1[d1[l1[-1]]] - l1[-1], pref2[len(nums2)] - pref2[d2[l1[-1]]] - l1[-1])) % mod
