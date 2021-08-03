class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def search(s):
            ans = [[s]]

            for i in range(1, len(s)):
                ans += [[s[:i]] + comb for comb in search(s[i:])]

            return ans

        a = search(s)
        r = 1
        for comb in a:
            # print(comb)
            if len(set(comb)) == len(comb):

                r = max(r, len(comb))

        return r
