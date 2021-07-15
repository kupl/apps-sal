class Solution:
    def numChanges(self, s:str, start :int, end: int) -> int:
        num = 0
        while start < end:
            if not s[start] is s[end]:
                num +=1
            start += 1
            end -= 1
        return num
    
    
    def palindromePartition(self, s: str, k: int) -> int:
        cache = [[0 for _ in range(len(s))] for _ in range(k)]
        size = len(s)
        for j in range(size - 1, -1, -1):
            cache[0][j] = self.numChanges(s, j, size - 1)
        
        for i in range(1, k):
            for j in range(size - 1 - i, -1, -1):
                cache[i][j] = min([cache[i-1][k + 1] + self.numChanges(s,j,k) for k in range(j, size - i) ])
        return cache[k-1][0]
                
                

