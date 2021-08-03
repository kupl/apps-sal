class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        seen = {i: i for i in range(1, 27)}
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if ch1 == ch2:
                continue
            else:
                move = ord(ch2) - ord(ch1) + 26 * (ord(ch1) > ord(ch2))
                last = seen[move]
                if last > k:
                    return False
                else:
                    seen[move] = last + 26

        return True
