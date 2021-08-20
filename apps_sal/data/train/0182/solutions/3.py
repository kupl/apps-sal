class Solution:

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_bounds = []
        lb = float('-inf')
        for h in height:
            lb = max(lb, h)
            l_bounds.append(lb)
        water = 0
        rb = float('-inf')
        for (lb, h) in zip(reversed(l_bounds), reversed(height)):
            rb = max(rb, h)
            water += min(lb, rb) - h
        return water
