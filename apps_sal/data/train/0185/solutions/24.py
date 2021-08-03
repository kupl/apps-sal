class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        result = set()
        for i in range(len(s) - k + 1):
            val = s[i:i + k]
            result.add(val)
        # print(result)
        if len(result) >= 2**k:
            return True
        else:
            return False
