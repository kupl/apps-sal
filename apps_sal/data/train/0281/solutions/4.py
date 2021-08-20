class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for (a, b) in zip(s, t):
            gap = ord(b) - ord(a)
            single = gap if gap >= 0 else 26 + gap
            if single == 0:
                continue
            if single not in dic:
                dic[single] = 0
            else:
                dic[single] += 1
            if dic[single] * 26 + single > k:
                return False
        return True
