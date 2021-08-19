class Solution:

    def findMinFibonacciNumbers(self, k: int) -> int:
        grid = [1, 1]
        last = 1
        while last < k:
            target = grid[-1] + grid[-2]
            if target > k:
                break
            else:
                grid.append(grid[-1] + grid[-2])
                last = grid[-1]
        res = 0
        ends = len(grid) - 1
        while k > 0:
            while grid[ends] > k:
                ends -= 1
            k -= grid[ends]
            ends -= 1
            res += 1
        return res
