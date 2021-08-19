class Solution:

    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        largest = [0] * 26
        for i in range(len(s)):
            diff = ord(t[i]) - ord(s[i])
            if diff == 0:
                continue
            elif diff < 0:
                diff += 26
            if largest[diff - 1] == 0:
                largest[diff - 1] = diff
            else:
                largest[diff - 1] += 26
            if largest[diff - 1] > k:
                return False
        return True
