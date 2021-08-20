class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            shift = 0
            if ord(t[i]) < ord(s[i]):
                shift = ord(t[i]) - ord(s[i]) + 26
            else:
                shift = ord(t[i]) - ord(s[i])
            cnt[shift] += 1
        for r in cnt:
            if (cnt[r] - 1) * 26 + r > k:
                return False
        return True
