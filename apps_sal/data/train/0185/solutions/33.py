class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        h = 0
        nums = set()
        
        if len(s) < k:
            return False
        
        for i in range(k):
            h <<= 1
            h += (1 if s[i] == '1' else 0)
        nums.add(h)
        
        for i in range(k, len(s)):
            h <<= 1
            h -= (1 if s[i - k] == '1' else 0) << k
            h += (1 if s[i] == '1' else 0)
            nums.add(h)
            
        return len(nums) == (1 << k)
