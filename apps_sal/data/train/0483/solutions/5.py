class Solution:
    def maxArea(self, items):
        '''
        Hi Lo Technique
        -----------------------
        Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate 
        (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and 
        (i, 0). Find two lines, which together with x-axis forms a container, such that the container
        contains the most water.
        -----------------------
        (1) Set lo and hi pointer at ends & bring them closer as results compared.
        (2) Get height for lo and hi. Keep the smallest.
        (3) Calcuate the area (smallest height * distance between lo and hi pointers) (height * width)
            If area is larger than currently stored max area, make it the max area.
        (4) Move the smallest pointer in.
        (5) Repeat steps 2-4
        (6) Return the max area
        '''
        max_area = 0
        lo = 0
        hi = len(items) - 1

        while(lo < hi):

            height_a = items[lo]
            height_b = items[hi]
            width = hi - lo
            height = min(height_a, height_b)

            area = height * width
            if area > max_area:
                max_area = area

            if height_a < height_b:
                lo += 1
            else:
                hi -= 1

        return(max_area)
