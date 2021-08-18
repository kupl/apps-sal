class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def countVowels(ct):
            if not ct['a'] % 2 and not ct['e'] % 2 and not ct['i'] % 2 and not ct['o'] % 2 and not ct['u'] % 2:
                return True
            return False

        for i in range(len(s)):
            ctr = collections.Counter(s[:len(s) - i])
            for j in range(i + 1):
                if j != 0:
                    ctr[s[j - 1]] -= 1
                    ctr[s[len(s) + j - i - 1]] += 1
                if countVowels(ctr):
                    return sum(ctr.values())
        return 0
