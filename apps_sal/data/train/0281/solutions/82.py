class Solution:

    def canConvertString(self, S: str, T: str, k: int) -> bool:
        if len(S) != len(T):
            return False
        dic = {}
        for (s, t) in zip(S, T):
            shift = (ord(t) - ord(s)) % 26
            if not shift:
                continue
            if shift not in dic:
                dic[shift] = 0
            dic[shift] += 1
            if shift + 26 * (dic[shift] - 1) > k:
                return False
        return True
