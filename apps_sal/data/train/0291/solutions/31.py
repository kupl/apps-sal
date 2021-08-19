class Solution:

    def numOddEvenSubarrays(self, arr: List[int], start: int) -> (int, int, int):
        if len(arr) == 0:
            return (0, 0, 0)
        if len(arr) == 1 or start == len(arr) - 1:
            return (0, 1, 0) if arr[start] % 2 == 0 else (1, 0, 0)
        (odd, even, oldOdd) = self.numOddEvenSubarrays(arr, start + 1)
        indOdd = (odd + oldOdd) % (10 ** 9 + 7)
        return (odd, even + 1, indOdd) if arr[start] % 2 == 0 else (even + 1, odd, indOdd)

    def numOfSubarrays(self, arr: List[int]) -> int:
        (odd, even, oldOdd) = self.numOddEvenSubarrays(arr, 0)
        total = (odd + oldOdd) % (10 ** 9 + 7)
        return total
