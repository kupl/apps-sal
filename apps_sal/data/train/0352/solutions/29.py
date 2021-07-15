#Longest increasing sequence.
# Instead, you can store all the words in a hashmap with their indexes. Now, for 
# Every word, try to delete one character and see if it is present in the map. But you need to sort the array first.
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chain = defaultdict(list)
        def checkPredecessor(w1, w2):
            for i in range(len(w2)):
                if w2[:i] + w2[i + 1:] == w1:
                    return True
            return False
        for idx, word in enumerate(words):
            chain[len(word)].append((word, idx))
        dp = [0] * len(words)
        
        i = 1
        while(i < 17):
            for word, dp_idx in chain[i]:
                if i - 1 in chain:
                    for checkWord, dp_jdx in chain[i - 1]:
                        if checkPredecessor(checkWord, word):
                            dp[dp_idx] = max(dp[dp_idx], 1 + dp[dp_jdx])
            i += 1
        return max(dp) + 1
            
        

