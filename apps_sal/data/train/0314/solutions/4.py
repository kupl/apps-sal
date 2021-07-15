class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        
        start = 0 
        while start < n and s[start] != '1':
            start += 1 
        if start == n:
            return 0 
        i = start
        count = 0
        while i < n and start < n:
            if s[i] == '1':
                count += i - start + 1
                count = count % (10**9 + 7)
                i += 1
                continue
            start = i
            while start < n and s[start] != '1':
                start += 1 
            i = start
        return count
