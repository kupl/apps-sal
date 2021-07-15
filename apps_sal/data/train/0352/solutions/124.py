# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
        
        
#         https://leetcode.com/problems/longest-string-chain/discuss/585044/C%2B%2B-Using-unordered_map-and-DP
# DP

# 1. sort words in increasing order of length
# 2. if len is same

# LIS

# dp[i] = longest word chain including index i
# return max(dp)

# dp[i] = max(dp[i], 1+ dp[j])
# len(words[j]) + 1 = len(words[i])
# ba, bda-> check all chars of j are in j in the same order

# O(n^2*16)





from collections import deque

def getKey(item):
    return len(item)

def isPred(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    q1 = deque(word1)
    q2 = deque(word2)
    while q1 and q2:
        if q1[0] == q2[0]:
            q1.popleft()
            q2.popleft()
        else:
            q2.popleft()
    if (not q1) and len(q2) <= 1:
        return True
    return False
    

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=getKey)
        dp = [1]*len(words)
        
        for i in range(1, len(dp)):
            for j in reversed(list(range(0, i))):
                if len(words[j]) == len(words[i]):
                    continue
                elif len(words[j]) + 1== len(words[i]):
                    if isPred(words[j], words[i]):
                        dp[i] = max(dp[i], 1+ dp[j])
                else:
                    break
        
        return max(dp)
        
        


# We can also think of thi problem as LIS problem 


# 1. Sort the words according to their length
# Input: [\"a\",\"b\",\"ba\",\"bca\",\"bda\",\"bdca\"]
# When you reach bdca ..check if dca is present..check if bca is present..check if bda is present..check if bdc is present
# 2. So store each word in a hashmap form lookup in O(1)

# 3. For each word in order of length, for each word2 which is word with one character removed, dp[word] = max(dp[word], dp[word2] + 1).
# The maxm element in the dp array is the answer.



# Clean implementation

# https://leetcode.com/problems/longest-string-chain/discuss/376724/C%2B%2B-Simple-clean





# Explaiantion:

# https://leetcode.com/problems/longest-string-chain/discuss/295182/C%2B%2B-Bottom-Up-DP-solution-(with-Explanation)

