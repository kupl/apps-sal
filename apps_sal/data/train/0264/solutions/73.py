class Solution:
    def maxLength(self, arr: List[str]) -> int:
        myQueue = collections.deque([('', 0)]) # word, index to start search from
        maxLen = 0
        
        while myQueue:
            word, start = myQueue.popleft()
            for i in range(start, len(arr)):
                newWord = word + arr[i]
                if self.isUnique(newWord):
                    maxLen = max(maxLen, len(newWord))
                    myQueue.append((newWord, i + 1))
        
        return maxLen
    
    def isUnique(self, s):
        return len(s) == len(set(s))

