class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        available, maxi = [0 if k < i else 1 + (k - i) // 26 for i in range(26)], 0
        for a, b in zip(s, t):
            if a == b:
                continue
            require = (26 + (ord(b) - ord('a')) - (ord(a) - ord('a'))) % 26
            if not available[require]:
                return False
            available[require] -= 1

            maxi = max(maxi, require)

        return maxi <= k
