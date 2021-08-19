class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        evenSum = 0
        oddSum = 0
        prefSum = 0
        ans = 0
        for ele in arr:
            prefSum = prefSum + ele
            '\n                prefix sum is odd\n            '
            if prefSum % 2 == 1:
                ans += evenSum + 1
                oddSum += 1
            else:
                ans += oddSum
                evenSum += 1
            ans %= 10 ** 9 + 7
        return ans
