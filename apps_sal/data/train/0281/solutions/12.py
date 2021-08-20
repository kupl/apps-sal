class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        ans = []
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            diff = ord(t[i]) - ord(s[i]) + (0, 26)[ord(t[i]) < ord(s[i])]
            dic[diff] = dic.get(diff, 0) + 1
            if diff + 26 * (dic[diff] - 1) > k:
                return False
        return True
