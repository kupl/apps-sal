class Solution:
    # https://leetcode.com/problems/can-convert-string-in-k-moves/discuss/826856/c%2B%2B-simple-sol...using-maps
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        lookup = collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] != t[i]:
                diff = (ord(t[i]) - ord(s[i]) + 26) % 26
                if diff > k:
                    return False
                lookup[diff] += 1

        for diff, freq in list(lookup.items()):
            maxCount = (freq - 1) * 26 + diff
            if maxCount > k:
                return False
        return True
