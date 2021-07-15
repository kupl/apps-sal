class Solution:
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        if minSize > len(s):
            return 0
            
        left = 0
        right = minSize - 1
        words = {}
        
        while left < len(s) - minSize + 1:
            word = s[left:right+1]
            while right < len(s) and right - left < maxSize and len(set(word)) <= maxLetters:
                if word not in words:
                    words[word] = 0
                words[word] += 1

                right += 1
                if right < len(s):
                    word += s[right]
            
            left += 1
            right = left + minSize - 1
        
        maxOccurences = 0
        for word in words:
            maxOccurences = max(maxOccurences, words[word])
        
        return maxOccurences
