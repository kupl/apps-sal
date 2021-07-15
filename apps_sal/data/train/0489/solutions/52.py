class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        numbers = list((num, i) for i, num in enumerate(A))
        numbers.sort()
        
        max_gap = 0
        min_element = numbers[0][1]
        
        for i in range(1, len(A)):
            min_element = min(min_element, numbers[i][1])
            max_gap = max(max_gap, numbers[i][1] - min_element)
        
        return max_gap
