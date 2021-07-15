class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if not s:
            return
        self.memo = {}
        return self.helper(0, len(s), k, s)
    
    def helper(self, i, j, k, s):
        if (i, j, k) in self.memo:
            return self.memo[(i, j, k)]
        if len(s) <= k:
            return 0
        if k == 1:
            min_change = self.cal_palindrome(s[i:j])
            self.memo[(i, j, k)] = min_change
            return min_change
        
        min_change = float('inf')
        for split in range(i+1, j):
            left = self.cal_palindrome(s[i:split])
            right = self.helper(split, j, k-1, s)
            if left+right < min_change:
                min_change = left+right
        self.memo[(i, j, k)] = min_change
        return min_change
    
    def cal_palindrome(self, s):
        if len(s) == 1:
            return 0
        if len(s) % 2 == 0:
            c_right = len(s) // 2 
            c_left = c_right -1
        else:
            c_left = len(s) // 2 - 1
            c_right = len(s) // 2 + 1
        count = 0
        while c_left >= 0:
            if s[c_left] != s[c_right]:
                count += 1
            c_left -= 1
            c_right += 1
        return count
            
        

