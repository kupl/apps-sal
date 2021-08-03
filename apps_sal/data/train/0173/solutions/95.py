from collections import Counter


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = Counter(x % k for x in arr)
        for x in count:
            y = -x % k
            if x == 0 and count[x] & 1:
                return False
            elif count[x] != count[y]:
                return False
        return True
