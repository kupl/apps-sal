class Solution:
    
    def is_palindrome(self, s):
        return bool(s == s[::-1])        
    
    def canConstruct(self, s: str, k: int) -> bool:
        r_map = dict()
        if k > len(s):
            return False
        for x in s:
            if x not in r_map:
                r_map[x] = 1
            else:
                r_map[x] += 1
        odd_count = 0
        for key in r_map:
            if r_map[key] % 2 == 1:
                odd_count += 1
        return odd_count <= k
