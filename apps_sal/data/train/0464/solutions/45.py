class Solution:

    def minOperations(self, n: int) -> int:
        arr = [2 * i + 1 for i in range(n)]
        target = sum(arr) / n
        opCount = 0
        ptr1 = 0
        ptr2 = len(arr) - 1
        while ptr1 < ptr2:
            stepSum = (arr[ptr2] - arr[ptr1]) // 2
            opCount += int(stepSum)
            ptr1 += 1
            ptr2 -= 1
        return opCount
