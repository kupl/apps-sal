class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        result = 0
        sumOdd = [0] * len(arr)
        sumEven = [0] * len(arr)
        if arr[0] % 2 == 1:
            sumOdd[0] = 1
            sumEven[0] = 0
        else:
            sumOdd[0] = 0
            sumEven[0] = 1
        for i in range(1, len(sumOdd)):
            if arr[i] % 2 == 0:
                sumOdd[i] = sumOdd[i - 1]
                sumEven[i] = sumEven[i - 1] + 1
            else:
                sumOdd[i] = sumEven[i - 1] + 1
                sumEven[i] = sumOdd[i - 1]
        return sum(sumOdd) % mod
