import math
from collections import Counter


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        curr = len(arr)
        target = math.ceil(len(arr) / 2)
        ans = 0
        counts = Counter(arr)
        for count in sorted(list(counts.values()), reverse=True):
            curr -= count
            ans += 1
            if curr <= target:
                return ans
