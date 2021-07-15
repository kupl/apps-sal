class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr = defaultdict(int)
        n = len(s)
        unique = set()
        max_freq = 0
        
        for i in range(n - minSize + 1):
            current_str = s[i:i+minSize]
            
            if len(set(current_str)) <= maxLetters:
                substr[current_str] += 1
                max_freq = max(max_freq, substr[current_str])
        
        
        return max_freq
