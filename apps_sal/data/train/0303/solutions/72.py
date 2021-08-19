class Solution:
    def partition(self, arr, k, index, memo):
        if len(arr) == 0:
            return 0

        if index in memo:
            return memo[index]

        maxNum = arr[0]
        maxSum = maxNum
        for i in range(1, min(k + 1, len(arr) + 1)):
            maxNum = max(maxNum, arr[i - 1])
            subarr = arr[:i]
            sumArr = self.partition(arr[i:], k, index + i, memo)
            # i is the size of the array you're examining
            sumArr += maxNum * (i)
            maxSum = max(sumArr, maxSum)

        memo[index] = maxSum
        return maxSum

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        memo = {}
        num = self.partition(arr, k, 0, memo)
        print(memo)
        return num
