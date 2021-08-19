class Solution:

    def minSteps(self, s: str, t: str) -> int:
        all_set = set(list(s)) | set(list(t))
        res = 0
        for x in all_set:
            res = res + abs(s.count(x) - t.count(x))
        res = res // 2
        return res
