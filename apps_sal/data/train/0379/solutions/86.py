class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 1000000007
        Dict1 = defaultdict(int)
        Dict2 = defaultdict(int)
        for i in range(len(nums1)):
            Dict1[nums1[i]] = i + 1
        for i in range(len(nums2)):
            Dict2[nums2[i]] = i + 1
        Dict3 = {}
        Dict4 = {}
        n1 = len(nums1)
        n2 = len(nums2)
        for i in nums1:
            if Dict1[i] > 0 and Dict2[i] > 0:
                Dict3[i] = Dict2[i]
                Dict4[i] = Dict1[i]

        @lru_cache(None)
        def go(i, pos):
            if pos == 0:
                if i >= n1:
                    return 0
                ans = 0
                if Dict1[nums1[i]] >= 1 and Dict2[nums1[i]] >= 1:
                    ans = max(ans, go(i + 1, pos) + nums1[i], go(Dict3[nums1[i]], (pos + 1) % 2) + nums1[i])
                else:
                    ans = max(ans, go(i + 1, pos) + nums1[i])
                return ans
            else:
                if i >= n2:
                    return 0
                ans = 0
                if Dict1[nums2[i]] >= 1 and Dict2[nums2[i]] >= 1:
                    ans = max(ans, go(i + 1, pos) + nums2[i], go(Dict4[nums2[i]], (pos + 1) % 2) + nums2[i])
                else:
                    ans = max(ans, go(i + 1, pos) + nums2[i])
                return ans
        return max(go(0, 0), go(0, 1)) % MOD
