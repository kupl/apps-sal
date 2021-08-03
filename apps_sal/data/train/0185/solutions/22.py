from itertools import permutations


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        for i in range(len(s) - k + 1):
            # print(s[i:i+k])
            if s[i:i + k] not in d:
                d.add(s[i:i + k])
                if len(d) == 2**k:
                    return True
        return False
