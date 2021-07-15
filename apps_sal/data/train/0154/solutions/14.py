class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        new_horizontal_cuts = [0] + sorted(horizontalCuts) +[h]
        new_vertical_cuts = [0] + sorted(verticalCuts) +[w]
        mod = int(1e9)+7
        max_height = 0
        max_width = 0
        for j in range(len(new_vertical_cuts)-1):
            if max_width < new_vertical_cuts[j+1]-new_vertical_cuts[j]:
                max_width = new_vertical_cuts[j+1]-new_vertical_cuts[j]
        for i in range(len(new_horizontal_cuts)-1):
            if max_height< new_horizontal_cuts[i+1]-new_horizontal_cuts[i]:
                max_height = new_horizontal_cuts[i+1]-new_horizontal_cuts[i]
        
        return (max_width*max_height)%mod
            

