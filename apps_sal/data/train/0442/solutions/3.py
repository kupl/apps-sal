class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def helper(row):
            for i in range(len(row) - 1, -1, -1):
                if row[i] == 1:
                    return len(row) - i - 1
            return len(row)
        arr = list(map(helper, grid))

        count = 0
        target = len(grid[0]) - 1
        for i in range(len(arr)):
            if arr[i] < target:
                found = False
                for j in range(i + 1, len(arr)):
                    if arr[j] >= target:
                        count += j - i
                        arr.insert(i, arr.pop(j))
                        found = True
                        break
                if not found:
                    return -1
            target -= 1
            
        return count
