class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        # return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)
    
#         if len(s) < k: return False
#         seen = {}
#         odd = 0
#         for char in s:
#             seen[char] = seen.get(char, 0) + 1
        
#         for val in seen.values():
#             if val % 2 == 1:
#                 odd += 1
        
#         if odd > k: return False
#         return True
        
        
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
