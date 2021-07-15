class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        [0, 2, 4, 5, 3, 1, 56, 0] -> input
        return the length of the longest subsequence of ascending numbers
        [1, 2, 0, 0, 0, 0, 0, 0]
        return max(dp)
        '''
        
        words.sort(key = lambda x : len(x))
        dp  = [1] * len(words)
        for i in range(len(words)):
            curr = words[i]
            for j in range(i):
                prev = words[j]
                if self.isPredecessor(curr, prev):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def isPredecessor(self, curr, prev):
        if len(curr) - len(prev) != 1: return False
        i = j = 0
        diff = False
        while i < len(curr) and j < len(prev):
            if curr[i] == prev[j]:
                i += 1
                j += 1
            else:
                if diff: return False
                diff = True
                i += 1
        return True
