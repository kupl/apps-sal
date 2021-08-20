class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        count = 0
        ans = 0
        c = Counter(arr)
        target = len(arr) / 2
        for (k, v) in sorted(list(c.items()), key=lambda x: x[1], reverse=True):
            count += v
            ans += 1
            if count >= target:
                return ans
        return 0
