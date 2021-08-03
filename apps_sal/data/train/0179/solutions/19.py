class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        m = {}

        def f(i, cur, length, dels):
            if i == len(s):
                return 0
            key = (i, cur, length, dels)
            if key in m:
                return m[key]
            del_cost = float('inf')
            if dels > 0:
                del_cost = f(i + 1, cur, length, dels - 1)
            keep = 0
            if s[i] == cur:
                extra = 0
                if length == 1 or len(str(length + 1)) > len(str(length)):
                    extra = 1
                keep = extra + f(i + 1, cur, length + 1, dels)
            else:
                keep = 1 + f(i + 1, s[i], 1, dels)
            m[key] = min(keep, del_cost)
            return m[key]
        return f(0, '', 0, k)
