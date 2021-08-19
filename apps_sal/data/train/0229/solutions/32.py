from collections import Counter


class Solution:

    def canReorderDoubled(self, A: List[int]) -> bool:
        count = Counter(A)
        for x in sorted(count, key=abs):
            if count[x] > count[2 * x]:
                return False
            count[2 * x] -= count[x]
        return True
