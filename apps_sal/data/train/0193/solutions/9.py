class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        import math
        from collections import Counter
        a = Counter(arr)
        b = list(a.values())
        b.sort(reverse=True)
        n = len(arr)
        summ = 0
        for i in range(len(b)):
            summ += b[i]
            if summ >= int(math.floor(0.5 * n)):
                return i + 1
        return None
