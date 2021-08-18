from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        counter = Counter(s)
        odd_counts = 0

        for char in counter:
            if counter[char] % 2 == 1:
                odd_counts += 1

        return odd_counts <= k
