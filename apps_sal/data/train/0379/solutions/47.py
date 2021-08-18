class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7.

        def csums(nums):
            arr = [None] * len(nums)
            for i in range(len(nums)):
                prev = 0 if i == 0 else arr[i - 1]
                arr[i] = prev + nums[i]
            return arr
        s1, s2 = csums(nums1), csums(nums2)
        mp1 = {v: idx for idx, v in enumerate(nums1)}
        mp2 = {v: idx for idx, v in enumerate(nums2)}
        sps = sorted(set(mp1.keys()) & set(mp2.keys()))
        ans = 0
        if not sps:
            ans = max(s1[-1], s2[-1]) % MOD
        else:
            idx1 = idx2 = None
            for idx, sp in enumerate(sps):
                idx1, idx2 = mp1[sp], mp2[sp]
                sum1 = s1[idx1] - (0 if idx == 0 else s1[mp1[sps[idx - 1]]])
                sum2 = s2[idx2] - (0 if idx == 0 else s2[mp2[sps[idx - 1]]])
                ans = (ans + max(sum1, sum2)) % MOD

            left1 = s1[-1] - s1[idx1]
            left2 = s2[-1] - s2[idx2]

            ans += max(left1, left2)
        return int(ans % MOD)
