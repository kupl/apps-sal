class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
            if k > len(s):
                return False
            elif k == len(s):
                return True

            seen = {}

            for letter in s:
                seen[letter] = seen.get(letter, 0) + 1

            singles = 0

            for key in seen:
                value = seen[key]
                if value % 2 == 1:
                    singles += 1

            return singles <= k

