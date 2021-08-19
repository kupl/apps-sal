class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        groups = {}
        result = -1
        for (i, a) in enumerate(arr):
            b = a - 1
            if b in groups:
                l = groups.pop(b)
                groups[a] = groups[b - l + 1] = l + 1
            else:
                groups[a] = 1
            if groups[a] - 1 == m:
                result = i
            c = a + 1
            if c in groups:
                l = groups.pop(a)
                r = groups.pop(c)
                groups[c + r - 1] = groups[a - l + 1] = l + r
                if r == m:
                    result = i
        return result
