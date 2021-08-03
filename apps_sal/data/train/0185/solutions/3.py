class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = set()
        for i in range(0, len(s) - k + 1):
            nums.add(s[i:i + k])
            if len(nums) == 2**k:
                return True
        return False
