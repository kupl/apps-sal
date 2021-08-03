class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def top_down(i, j, memo):
            if (i, j) not in memo:
                # If length of current stick is less than or equal to one, we can't cut any further so cost will be zero.
                if j - i <= 1:
                    return 0
                memo[(i, j)] = float('inf')
                for c in cuts:
                    # If c is not in the range of (i, j) exclusive, cut cannot be performed.
                    if c > i and c < j:
                        memo[(i, j)] = min(memo[(i, j)], j - i + top_down(i, c, memo) + top_down(c, j, memo))
            # if no valid cutting position, return 0 otherwise return optmal solution.
            return memo[(i, j)] if memo[(i, j)] != float('inf') else 0
        return top_down(0, n, dict())
