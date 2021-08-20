class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        memoOdd = arr[0] % 2
        memoEven = -(arr[0] % 2 - 1)
        memoOddSum = memoOdd
        for i in range(1, len(arr)):
            memoOdd_temp = memoOdd
            memoEven_temp = memoEven
            memoOdd = memoOdd_temp * -(arr[i] % 2 - 1) + memoEven_temp * (arr[i] % 2) + arr[i] % 2
            memoEven = memoOdd_temp * (arr[i] % 2) + memoEven_temp * -(arr[i] % 2 - 1) - (arr[i] % 2 - 1)
            memoOddSum += memoOdd
        return memoOddSum % 1000000007
