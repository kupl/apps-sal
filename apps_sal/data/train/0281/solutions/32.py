class Solution:
    def canConvertString(self, s, t, k):
        n, m = len(s), len(t)
        if n != m:
            return False
        cnt = [0] * 26
        for i in range(n):
            if s[i] == t[i]:
                continue
            diff = (ord(t[i]) - ord(s[i])) % 26
            if cnt[diff] * 26 + diff > k:
                return False
            cnt[diff] += 1
        return True
