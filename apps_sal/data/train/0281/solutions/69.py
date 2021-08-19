class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in range(len(s)):
            if s[i] != t[i]:
                diff = -1 * (ord(s[i]) - ord(t[i]))
                if diff < 0:
                    diff = 26 + diff
                if diff in hash_map:
                    hash_map[diff] += 1
                    diff += (hash_map[diff] - 1) * 26
                else:
                    hash_map[diff] = 1
                if diff > k:
                    return False
        return True
