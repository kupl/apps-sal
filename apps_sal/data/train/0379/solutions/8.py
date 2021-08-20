class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        prev = collections.defaultdict(set)
        MOD = 10 ** 9 + 7
        if not nums1:
            return sum(nums2)
        elif not nums2:
            return sum(num1)
        ans = 0
        combined = sorted(set(nums1 + nums2))
        dp = collections.defaultdict(lambda: 0)
        dp[-1] = 0
        for i in range(len(nums1)):
            if i == 0:
                prev[nums1[i]].add(-1)
            prev[nums1[i]].add(nums1[i - 1])
        for i in range(len(nums2)):
            if i == 0:
                prev[nums2[i]].add(-1)
            prev[nums2[i]].add(nums2[i - 1])
        for num in combined:
            for p in prev[num]:
                dp[num] = max(dp[p] + num, dp[num])
                ans = max(ans, dp[num])
        return ans % MOD
