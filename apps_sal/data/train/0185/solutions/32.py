class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        a = 2 ** k
        for i in range(len(s) - k + 1):
            tmp = s[i:i + k]
            if tmp not in d:
                d.add(tmp)
                if len(d) == a:
                    return True
        return False
