from collections import Counter


class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        evens = 0
        odds = 0
        for (key, value) in counter.items():
            if value % 2 == 0:
                evens += 1
            else:
                odds += 1
        return k >= odds and len(s) >= k
