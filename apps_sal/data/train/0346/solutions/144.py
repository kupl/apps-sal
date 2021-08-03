class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        P = [0]
        for n in nums:
            P.append(P[-1] + n % 2)

        from collections import Counter
        count = Counter()
        ans = 0
        for p in P:
            ans += count[p]
            count[p + k] += 1

        return ans
