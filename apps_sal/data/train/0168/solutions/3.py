from collections import defaultdict


class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        d = defaultdict(int)
        if len(s) < k:
            return False
        for char in s:
            d[char] += 1
        odd = 0
        for key in d:
            print(key)
            if d[key] % 2 != 0:
                odd += 1
        return odd <= k
