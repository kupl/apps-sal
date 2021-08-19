class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        combinations = 2 ** k
        seen = set()
        for i in range(len(s) - k + 1):
            temp = s[i:i + k]
            if temp not in seen:
                seen.add(temp)
                combinations -= 1
                if combinations == 0:
                    return True
        return False
