class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:

        if len(s) != len(t):
            return False

        def aIntoB(a, b) -> int:
            return (ord(b) - ord(a)) % 26

        moves = [k // 26] * 26
        for i in range((k % 26) + 1):
            moves[i] += 1

        for a, b in zip(s, t):
            if a == b:
                continue

            moves[aIntoB(a, b)] -= 1
            if moves[aIntoB(a, b)] < 0:
                return False

        return True
