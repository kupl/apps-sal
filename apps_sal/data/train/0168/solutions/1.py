class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        from collections import Counter
        if len(s) < k:
            return False
        oc = 0
        for _, val in list(Counter(s).items()):
            if val % 2 == 1:
                oc += 1
        return False if oc > k else True
