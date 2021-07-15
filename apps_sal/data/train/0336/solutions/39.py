from collections import Counter

class Solution:
    
    def minSteps(self, s: str, t: str) -> int:
        one, two = Counter(s), Counter(t)
        return sum({k: abs(one[k] - two[k]) for k in one | two}.values()) // 2
        

