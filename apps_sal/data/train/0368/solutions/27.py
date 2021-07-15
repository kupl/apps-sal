class Solution:

    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        temp = [0] * len(satisfaction)
        output = 0
        satisfaction.sort()
        for i, _ in enumerate(satisfaction):
            for j, s in enumerate(satisfaction[i:]): 
                temp[i] += s*(j+1)

        for s in temp: 
            if s > output: 
                output = s

        return output

