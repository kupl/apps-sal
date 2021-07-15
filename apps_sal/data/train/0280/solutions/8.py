class Solution:
    def __init__(self):
        self.table = {}
        
    def palindromePartition(self, s: str, k: int) -> int:
            
        def distanceToPalindrome(subs):
            k = 0
            for i in range(int(len(subs)/2)):
                if subs[i] != subs[len(subs)-i-1]:
                    k += 1
            return k
                    
        if len(s) == 1:
            return 0
        
        if k == 1:
            return distanceToPalindrome(s)
        
        lens = len(s)
        if lens in self.table:
            if k in self.table[lens]:
                return self.table[lens][k]
                           
        out = len(s)          
        for i in range(1, len(s)):
            out = min(out, distanceToPalindrome(s[:i]) + self.palindromePartition(s[i:], k-1))
            
        if lens not in self.table:
            self.table[lens] = {}
        self.table[lens][k] = out
                                   
        return out
