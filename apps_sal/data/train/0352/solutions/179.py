class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Note: order does not matter for this problem
        words = sorted(words, key=lambda word: len(word))
        # Once we've sorted words by length, we need an efficient way to
        # check if a longer word can be generated from a shorter word
        # We can simply do a char by char comparison which is O(W), where W 
        # is the maximum length of a word
        # You have to do this for all strings of length 1 less than current string's length
        # If you find a match, then increment the dp value
        n = len(words)
        if n == 1:
            return 1
        
        ans = 1
        # dp[i] is the length of the longest chain ending at i
        dp = [1]*n
        
        # Check if string at i can be generated from string at j
        def match(i, j):
            # This function assumes that len(words[i]) - len(words[j]) == 1
            idx_i = 0
            idx_j = 0
            skipped = False
            while idx_j < len(words[j]):
                if words[i][idx_i] != words[j][idx_j]:
                    if skipped:
                        return False
                    skipped = True
                    idx_i += 1
                else:
                    idx_i += 1
                    idx_j += 1
            return True
        
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if len(words[i]) - len(words[j]) > 1:
                    break
                elif len(words[i]) - len(words[j]) == 1:
                    if match(i, j):
                        dp[i] = max(dp[i], dp[j] + 1)
                        ans = max(ans, dp[i])
                else:
                    pass
            
        return ans
