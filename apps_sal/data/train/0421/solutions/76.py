class Solution:

    def lastSubstring(self, s: str) -> str:
        index = {c: i for (i, c) in enumerate(sorted(set(s)))}
        (radix, opt, curr, i_0) = (len(index), 0, 0, 0)
        for i in range(len(s) - 1, -1, -1):
            curr = index[s[i]] + curr / radix
            if curr > opt:
                (opt, i_0) = (curr, i)
        return s[i_0:]
