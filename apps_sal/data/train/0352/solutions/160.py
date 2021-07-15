class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)
        
        def is_predecessor(word1: str, word2: str) -> bool:
            if (len(word1) + 1 == len(word2)):
                diffCount = 0
                i, j = 0, 0
                while (i < len(word1) and j < len(word2)):
                    if (word1[i] == word2[j]):
                        i += 1
                        j += 1
                    elif (diffCount == 0):
                        j += 1
                        diffCount = 1
                    else:
                        return False
                return True
            return False
        
        def backtracking(start: int, count: int) -> int:
            if (start in memo):
                return memo[start]
            
            sublongest = count
            for i in range(start + 1, N):
                if (is_predecessor(words[start], words[i])):
                    sublongest = max(sublongest, backtracking(i, count + 1))
            memo[start] = sublongest
            return sublongest
        
        words.sort(key = lambda x: (len(x), x))
        
        memo = dict()
        longest = 0
        for i in range(N):
            longest = max(longest, backtracking(i, 1))
        return longest
