class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if len(s) < k:
            return False

        seen = {}
        odd = 0

        for letter in s:
            seen[letter] = seen.get(letter, 0) + 1

        for value in seen.values():
            if value % 2 != 0:
                odd += 1

        if odd > k:
            return False

        return True
