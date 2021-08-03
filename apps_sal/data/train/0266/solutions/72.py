from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        l, r = {}, Counter(s)
        ans = 0
        for i in range(len(s) - 1):
            # Add s[i] to l
            if s[i] in l:
                l[s[i]] += 1
            else:
                l[s[i]] = 1
            # Remove s[i] from r
            if s[i] in r:
                r[s[i]] -= 1
                if r[s[i]] == 0:
                    del r[s[i]]
            if len(l) == len(r):
                #print(i, l, r)
                ans += 1
        return ans
