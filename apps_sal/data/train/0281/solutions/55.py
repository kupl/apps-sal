class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        used = {}
        for i in range(len(s)):
            diff = ord(s[i]) - ord(t[i])
            if diff == 0:
                continue

            i = (26 - diff) if diff > 0 else abs(diff)
            if i > k:
                return False

            if i not in used:
                used[i] = 1
            else:
                move = used[i] * 26 + i
                if move > k:
                    return False
                else:
                    used[i] += 1

        return True
