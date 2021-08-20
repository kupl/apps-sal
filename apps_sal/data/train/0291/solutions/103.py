class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        (s, d, ans) = (0, 0, 0)
        for n in arr:
            if n % 2:
                (s, d) = (d, s)
                s += 1
            else:
                d += 1
            ans += s
        return ans % 1000000007
