class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        for i in range(len(arr)):
            arr[i] %= 2
        n = len(arr)
        dp = []
        ones = 0
        zeroes = 0
        for i in arr:
            if not dp:
                dp.append(i)
            else:
                dp.append(dp[-1] + i)
            dp[-1] %= 2
            if dp[-1] == 0:
                zeroes += 1
            else:
                ones += 1
        total = n * (n + 1) // 2
        total -= ones * (ones - 1) // 2
        total -= zeroes + zeroes * (zeroes - 1) // 2
        return total % mod
