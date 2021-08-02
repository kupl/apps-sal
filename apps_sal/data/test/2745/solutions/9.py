from collections import Counter
from copy import deepcopy
class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        wordCounter = Counter(words)
        longest = len(words[0])
        lenSubStr = longest * len(words)
        n = len(s)

        idx = []
        for i in range(0, min(longest, n - lenSubStr + 1)):
            if i in idx:
                continue
            cnt = {}
            j = i
            start = i
            while start + lenSubStr <= n:
                word = s[j:j+longest]
                j += longest
                if word not in wordCounter:
                    start = j
                    cnt.clear()
                else:
                    if word in cnt:
                        cnt[word] += 1
                    else:
                        cnt[word] = 1
                        
                    while cnt[word] > wordCounter[word]:
                        cnt[s[start: start + longest]] -= 1
                        start += longest
                        
                    if j - start == lenSubStr:
                        idx.append(start)

        return list(idx)
                    
                
                
        
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        