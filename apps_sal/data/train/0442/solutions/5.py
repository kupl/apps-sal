class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        def countzeros(row):
            zeros = 0
            while(row):
                new = row.pop()
                if new == 0:
                    zeros += 1
                else:
                    return(zeros)
            return(zeros)
        zeros = [countzeros(i) for i in grid]
        print(zeros)
        row = 0
        ops = 0
        while(len(zeros)):
            found = False
            for i in range(len(zeros)):
                if zeros[i] >= n - 1 - row:
                    ops += i
                    zeros.remove(zeros[i])
                    row += 1
                    found = True
                    break
            if not found:
                return(-1)
        return(ops)
