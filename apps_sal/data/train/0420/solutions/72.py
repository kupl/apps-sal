class Solution:

    def check1(self, ct):
        if not ct['a'] % 2 and (not ct['e'] % 2) and (not ct['i'] % 2) and (not ct['o'] % 2) and (not ct['u'] % 2):
            return True
        return False

    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            ctr = collections.Counter(s[0:i])
            for j in range(len(s) - i + 1):
                if j != 0:
                    ctr[s[j - 1]] -= 1
                    ctr[s[i + j - 1]] += 1
                if self.check1(ctr):
                    return i
        return 0
