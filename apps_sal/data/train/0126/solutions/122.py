from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = defaultdict(int)
        for size in range(minSize, maxSize+1):
            for i in range(len(s)-size+1):
                substring = s[i:i+size]
                if len(set(substring)) <= maxLetters:
                    count[substring] += 1
        if count:
            return max(count.values())      
        return 0
