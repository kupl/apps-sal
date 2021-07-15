class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def dfs(start, end):
            if (start, end) in cache:
                return cache[(start, end)]
            min_val = float('inf')
            cut_found = False
            for c in cuts:
                if c > start and c < end: # Important!!! check the boundary condition
                    left_val = dfs(start, c)
                    # print ('Left', left_val, 'C', c)
                    right_val = dfs(c, end)
                    # print ('Right', right_val, 'C', c)
                    min_val = min(min_val, left_val + right_val)
                    # print (\"Left and Right\", left_val, right_val)
                    # print (\"MIN VAL:n \", min_val)
                    cut_found = True
                
            if not cut_found: # If no cut is found we know that the stick cannot be split more
                cache[(start, end)] = 0
            else:
                cache[(start, end)] = end - start + min_val
            return cache[(start, end)]

        cache = defaultdict(int)
        return dfs(0, n)
