from itertools import product


class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        p = product('01', repeat=k)
        for sub in p:
            if s.find(''.join(sub)) == -1:
                return False
        return True
