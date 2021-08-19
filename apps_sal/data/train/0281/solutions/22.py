class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0 for i in range(26)]
        for (a, b) in zip(s, t):
            cnt[(ord(b) - ord(a)) % 26] += 1
        for i in range(1, 26):
            if cnt[i] > 0 and (cnt[i] - 1) * 26 + i > k:
                return False
        return True
