class Solution:
    def numSteps(self, s: str) -> int:
        i, mid_zero = 0 , 0 
        for j in range(1, len(s)):
            if s[j] == '1':
                mid_zero += j -i - 1
                i = j
        if i == 0:
            return len(s)-1
        return mid_zero + 1 + len(s)

