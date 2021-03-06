class Solution:

    def maxUniqueSplit(self, s: str) -> int:

        def helper(s, strings=set()):
            leng_s = len(s)
            leng_set = len(strings)
            if leng_s == 1 and s in strings:
                return 0
            else:
                ans = leng_set + 1
                for i in range(1, leng_s):
                    substr = s[:i]
                    if substr not in strings:
                        ans = max(ans, helper(s[i:], strings | {substr}))
                return ans
        return helper(s)
