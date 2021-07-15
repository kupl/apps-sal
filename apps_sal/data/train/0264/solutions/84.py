class Solution:
    def __init__(self):
        self._maxLength = 0
        
    def maxLength(self, arr: List[str]) -> int:
        self.uniqueLengths(arr, [])
        return self._maxLength
    
    def uniqueLengths(self, arr, concat):
        if not self.hasUniqueChars(''.join(concat)):
            return
        
        self._maxLength = max(self._maxLength, len(''.join(concat)))
        
        for i in range(len(arr)):
            concat.append(arr[i])
            self.uniqueLengths( arr[i+1:], concat)
            concat.pop()
    
    def hasUniqueChars(self, concat):
        counter = Counter(concat)
        return all([x == 1 for x in counter.values()])
