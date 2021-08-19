class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        ans = [0]

        def split(curr, ind):
            if ind >= len(s):
                return len(curr)
            for i in range(ind + 1, len(s) + 1):
                tmp = curr.copy()
                tmp.add(s[ind:i])
                s1 = split(tmp, i)
                ans[0] = max(ans[0], s1)
            return len(curr)
        split(set(), 0)
        return ans[0]
