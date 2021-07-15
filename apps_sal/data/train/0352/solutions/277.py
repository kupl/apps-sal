class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        words_len = len(words)
        
        def predecessor(word, candidate):
            if len(word) != len(candidate)+1:
                return False
            j = 0
            for i, c in enumerate(word):
                if i > j + 1 or j == len(candidate):
                    break
                if c == candidate[j]:
                    j += 1
            return j == len(candidate)
        
        
        dp = [1] * words_len
        for i in range(words_len):
            # cur_possibles = makePossibles(words[i])
            curLen = len(words[i])
            for j in range(i - 1, -1, -1):
                if len(words[j]) < curLen-1:
                    break
                if predecessor(words[i], words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])
                
            
        
        return max(dp)
        
        # makePossibles(words[2])
        # getAdjacents(words[2], 2)
        # print(words)

