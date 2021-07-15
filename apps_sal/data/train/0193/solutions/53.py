class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = dict()
        for x in arr:
            d.setdefault(x, 0)
            d[x] += 1
        c = sorted(d.values(), reverse=True)
        for i in range(1, len(c)):
            c[i] += c[i-1]
        
        for i, x in enumerate(c):
            if x >= len(arr) // 2:
                return i + 1
