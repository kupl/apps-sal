class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # from https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414716/Python-two-solutions%3A-backtracking-and-A*-search
        # backtracking
        # fill all spaces with all possible sizes one by one
        # like stacking in storage, put one box at a time
        # that covers the floor, i.e. no gap underneath, e.g. box-1 in example 3
        # (examples call it skyline filling)
        # algo:
        # maintain an array of heights with unit widths
        # each iteration, fill the min height space
        # not greedily, but try all sizes
        # pick larger size first to slightly improve search
        # so that smaller size resulting in more boxes than a found solution
        # can be skipped
        
        self.best = m * n # max number, also guaranteed to fill
        
        def dfs(heights, count):
            if min(heights) == n: # filled out all unit columns
                self.best = min(self.best, count)
                return 
            if count >= self.best: # a solution with count already exists, not point searching
                return 
            
            # find minimum height spacce to fill 
            min_height = min(heights)
            idx = heights.index(min_height)
            right_end = idx + 1
            while right_end < m and heights[right_end] == min_height:
                right_end += 1
            max_possible_box = min(right_end-idx, n - min_height)
            
            # now fill with boxes and backtrack
            for box_size in range(max_possible_box, 0, -1):
                new_heights = heights[:]
                for i in range(box_size):
                    new_heights[idx+i] += box_size
                dfs(new_heights, count + 1)
            
        dfs([0] * m, 0)
        return self.best
