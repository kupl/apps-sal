class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 1000000000 + 7

        def findMaxSubarray(mat: List[int]) -> int:
            maxSum = 0
            currSum = 0

            for i in mat:
                currSum = max(currSum + i, i)
                maxSum = max(maxSum, currSum)
            return maxSum

        a = arr.copy()
        if k == 1:
            return findMaxSubarray(a)

        a.extend(arr)
        subMax = findMaxSubarray(a)

        total = 0
        for n in arr:
            total += n

        if total > 0:
            return (subMax + (k - 2) * total) % MOD
        else:
            return subMax % MOD
