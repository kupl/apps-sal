class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}

        for el in arr:
            if d.get(el):
                d[el] += 1
            else:
                d[el] = 1

        s = sorted(d.values())
        l = len(arr) / 2
        c = 0

        for i in reversed(range(len(s))):
            l -= s[i]
            c += 1
            if l <= 0:
                break

        return c
