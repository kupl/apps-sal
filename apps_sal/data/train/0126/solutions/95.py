class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        if minSize > len(s):
            return 0
            
        words = {}
        for size in range(minSize, maxSize + 1):
            left = 0
            right = size - 1
            while right < len(s):
                word = s[left:right + 1]
                if len(set(word)) <= maxLetters:
                    if word not in words:
                        words[word] = 0
                    words[word] += 1
                left += 1
                right += 1
        
        maxOccurences = 0
        for word in words:
            maxOccurences = max(maxOccurences, words[word])
        
        return maxOccurences
