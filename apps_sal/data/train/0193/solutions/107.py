from collections import Counter


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        tot = n = len(arr)
        count = Counter(arr)
        res = 0
        for (k, v) in sorted(count.items(), key=lambda x: -x[1]):
            tot -= v
            res += 1
            if tot <= n // 2:
                return res
        return n
