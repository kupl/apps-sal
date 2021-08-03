class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        memoOdd = [arr[0] % 2]
        memoEven = [-(arr[0] % 2 - 1)]

        for i in range(1, len(arr)):
            memoOdd.append(memoOdd[i - 1] * (-(arr[i] % 2 - 1)) + memoEven[i - 1] * (arr[i] % 2) + arr[i] % 2)
            memoEven.append(memoOdd[i - 1] * (arr[i] % 2) + memoEven[i - 1] * (-(arr[i] % 2 - 1)) - (arr[i] % 2 - 1))

        return sum(memoOdd) % 1000000007
