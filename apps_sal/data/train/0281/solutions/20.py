class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        numMoves = [int(k / 26)] * 26
        for i in range(1, (k % 26) + 1):
            numMoves[i] += 1

        for i in range(len(t)):
            shift = (ord(t[i]) - ord(s[i])) % 26
            if shift == 0:
                continue
            numMoves[shift] -= 1
            if numMoves[shift] < 0:
                return False

        return True
