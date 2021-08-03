class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        P = [0]
        for x in nums:
            P.append(x + P[-1])
        aux = {}
        ans = N = len(nums)
        for j, pref in enumerate(P):
            aux[pref % p] = j
            c = (pref - P[-1]) % p
            if c in aux:
                ans = min(ans, j - aux[c])
        return ans if ans < N else -1
