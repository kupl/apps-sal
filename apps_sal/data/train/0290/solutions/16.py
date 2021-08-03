class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        if cuts == None or len(cuts) == 0:
            return 0

        dp = defaultdict(int)

        def dfs(start, end):
            if (start, end) in dp:
                return dp[(start, end)]

            min_val = float('inf')
            cut_found = False
            for c in cuts:
                if c > start and c < end:  # Important!!! check the boundary condition
                    left_val = dfs(start, c)
                    right_val = dfs(c, end)
                    min_val = min(min_val, left_val + right_val)
                    cut_found = True

            if not cut_found:  # If no cut is found we know that the stick cannot be split more
                dp[(start, end)] = 0
            else:
                dp[(start, end)] = end - start + min_val
            return dp[(start, end)]

        return dfs(0, n)
