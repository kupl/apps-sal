class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        memo = {0: 0}
        dic = dict(list(zip('aeiou', list(range(5)))))
        (curr, ans) = (0, 0)
        for (k, v) in enumerate(s, 1):
            if v in dic:
                curr ^= 1 << dic[v]
            if curr in memo:
                ans = max(ans, k - memo[curr])
            else:
                memo[curr] = k
        return ans
