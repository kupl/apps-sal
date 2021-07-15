class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # self.cache = [ [-1] * (len(text2) + 1) for _ in range(len(text1))]
        # for row in self.cache:
        #     row[-1] = 0
        # self.cache.append([ 0 ] * (len(text2) + 1))
        
        self.cache = [ [-1] * len(text2) for _ in range(len(text1))]
        
        def findSubsequence(idx1, idx2):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            if self.cache[idx1][idx2] != -1:
                return self.cache[idx1][idx2]
            res = 0
            if text1[idx1] == text2[idx2]:
                res = 1 + findSubsequence(idx1 + 1, idx2 + 1)
            else:
                res = max(
                    findSubsequence(idx1 + 1, idx2),
                    findSubsequence(idx1, idx2 + 1)
                )
            self.cache[idx1][idx2] = res
            return res
        
        return findSubsequence(0, 0)

