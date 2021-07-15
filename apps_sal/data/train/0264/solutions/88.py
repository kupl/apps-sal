from collections import defaultdict

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.longest = 0
        def valid(s):
            d = defaultdict(int)
            for char in s:
                d[char] += 1
                if d[char] == 2:
                    return False
            return True
        
        def backtrack(curr, ind):
            if ind == len(arr):
                if len(curr) > self.longest: self.longest = len(curr)
                return
            for i in range(ind, len(arr)):
                temp = curr+arr[i]
                if valid(temp):
                    backtrack(curr+arr[i], i + 1)
            
            if len(curr) > self.longest: self.longest = len(curr)
            return
                
        for i in range(len(arr)):
            if valid(arr[i]):
                backtrack(arr[i], i)
        
        return self.longest
