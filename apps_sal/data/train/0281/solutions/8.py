class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        diff = []
        res = []
        diff.extend((ord(t[i]) - ord(s[i]) + [0, 26][ord(t[i]) < ord(s[i])] for i in range(len(s)) if s[i] != t[i]))
        counter = Counter(diff)
        res.extend((key + 26 * i for key in counter for i in range(counter[key])))
        return all([r <= k for r in res])
