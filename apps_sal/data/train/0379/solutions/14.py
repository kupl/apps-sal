class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        prev = collections.defaultdict(set)
        MOD = 10 ** 9 + 7
        if not nums1:
            return sum(nums2)
        elif not nums2:
            return sum(num1)
        ans = 0
        
        dp = collections.defaultdict(lambda: 0)
        dp[-1] = 0
        
        for i in  range(len(nums1)):
            if i == 0:
                prev[nums1[i]].add(-1)
            prev[nums1[i]].add(nums1[i - 1])
            
        for i in range(len(nums2)):
            if i == 0:
                prev[nums2[i]].add(-1)
            prev[nums2[i]].add(nums2[i - 1])
        i = j = 0
        while i < len(nums1) or j < len(nums2):
            target = -1
            if j >= len(nums2) or (i < len(nums1) and nums1[i] < nums2[j]):
                target = nums1[i]
                i += 1
            else:
                target = nums2[j]
                j += 1
        
            for p in prev[target]:
                dp[target] = max(dp[p] + target, dp[target])
                ans = max(ans, dp[target])
        return ans % MOD

