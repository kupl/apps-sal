class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_seq(word1, word2):
            if len(word2)!=len(word1)+1:
                return False
            L=len(word2)
            for idx in range(L):
                if word1==word2[:idx]+word2[idx+1:]:
                    return True
            return False
        
        L=len(words)
        dp=[1 for w in words]
        words=sorted(words, key=lambda x:len(x))
        for idx in range(L):
            word2=words[idx]
            for j in range(idx):
                word1=words[j]
                if is_seq(word1, word2):
                    dp[idx]=max(dp[idx], dp[j]+1)
        return max(dp)
