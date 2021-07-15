from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counter = Counter(s)
        count = 0
        for key in counter:
            if counter[key] % 2 == 1:
                count += 1
        return count <= k
        

