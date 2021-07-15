class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = [1]*len(words)
        
        possible_pred = [0]*len(words)
        for i in range(len(words)-1, -1, -1):
            cur_word = words[i]
            cur_length = len(cur_word)
            for j in range(i+1, len(words)):
                if len(words[j]) == cur_length+1 and cur_word in possible_pred[j]:
                    dp[i] = max(dp[i], dp[j]+1)
            pred = set()
            for k in range(len(cur_word)):
                pred.add(cur_word[0:k]+cur_word[k+1:])
            possible_pred[i] = pred
        return max(dp)
                    

