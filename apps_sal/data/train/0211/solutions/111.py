from functools import lru_cache


class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        @lru_cache(None)
        def helper(s, n):
            # print(s, n)
            ts = set()
            cs = ''
            for i in range(len(s)):
                cs += s[i]
                if n % 2 == 1:
                    if cs in ts:
                        # print(ts, cs)
                        return -1
                    else:
                        ts.add(cs)
                        cs = ''
                    n = n // 2
                else:
                    n = n // 2
                    continue
            if cs != '':
                if cs in ts:
                    # print(ts, cs)
                    return -1
                else:
                    ts.add(cs)
            # print(ts)
            return len(ts)

        r = -1
        for i in range(0, 2**(len(s) - 1)):
            r = max(r, helper(s, i))
        return r
