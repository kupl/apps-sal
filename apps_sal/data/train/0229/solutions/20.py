import collections


class Solution:

    def canReorderDoubled(self, a: List[int]) -> bool:
        count = collections.Counter(a)
        for elem in sorted(a, key=abs):
            if count[elem] == 0:
                continue
            if count[2 * elem] == 0:
                return False
            count[elem] -= 1
            count[2 * elem] -= 1
        return True
