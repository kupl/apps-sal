class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        half = len(arr) // 2
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
        lst = sorted(list(d.values()), reverse=True)
        accum = 0
        res = 0
        for item in lst:
            if accum < half:
                accum += item
                res += 1
        return res
