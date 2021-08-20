class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        (seen, total) = (set(), 2 ** k)
        for i in range(len(s) - k + 1):
            if s[i:i + k] not in seen:
                seen.add(s[i:i + k])
                total -= 1
                if total == 0:
                    return True
        return False
