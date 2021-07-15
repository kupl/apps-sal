import numpy as np

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        output = []
        length = len(satisfaction)
        satisfaction_srt = sorted(satisfaction)
        
        for i in range(length):
            satisfaction = satisfaction_srt[i:]
            time = list(range(1,length+1-i))
            output.append(np.dot(time,satisfaction))
        
        if max(output) < 0:
            return 0
        else:
            return max(output)
        
ans = Solution()
ans.maxSatisfaction([-1,-8,0,5,-7])
