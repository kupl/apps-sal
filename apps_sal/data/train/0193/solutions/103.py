class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        n, half = len(arr), len(arr) // 2
        seen = set()
        for i in arr:
            d[i] = d.get(i, 0) + 1
        d = sorted(d.items(), key=lambda x: -x[1])
        for k, v in d:
            if n - v > half:
                n -= v
                seen.add(k)
            else:
                seen.add(k)
                return len(seen)
