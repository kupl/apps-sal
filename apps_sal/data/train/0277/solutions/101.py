class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        if not light: return int()
        
        answer = right = int()
        
        for i, light in enumerate(light):
            right   = max(right, light)
            if i + 1 == right:
                answer += 1
        
        return answer
