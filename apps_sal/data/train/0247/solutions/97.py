class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        l = 0
        currentSum = 0
        res = -1
        record = [-1] * len(arr)
        for r in range(len(arr)):
            currentSum += arr[r]
            while currentSum > target and l < r:
                currentSum -= arr[l]
                l += 1
            if currentSum == target:
                curr = r - l + 1
                print(curr)
                if record[l - 1] != -1:
                    res = curr + record[l - 1] if res == -1 else min(res, curr + record[l - 1])
                record[r] = curr if record[r - 1] == -1 else min(record[r - 1], curr)
            else:
                record[r] = record[r - 1]
        return res
