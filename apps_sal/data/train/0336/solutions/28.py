class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1
        s_count = collections.Counter(s)  # b=2 a=1
        for c in t:
            if c in s_count:
                s_count[c] -= 1
            if s_count[c] == 0:
                del(s_count[c])
        total = 0
        for val in list(s_count.values()):
            total += val
        return total
