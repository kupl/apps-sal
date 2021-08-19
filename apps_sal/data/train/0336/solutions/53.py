from collections import defaultdict


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        h = defaultdict(int)
        k = defaultdict(int)
        for i in s:
            h[i] += 1
        for j in t:
            k[j] += 1
        ans = 0
        for i in h:
            ans += h[i] - k[i] if h[i] - k[i] > 0 else 0
            # print(h[i],k[i],i)
        return ans
