class Solution:

    def countTriplets(self, arr: List[int]) -> int:

        def xor(arr):
            xor = 0
            for a in arr:
                xor ^= a
            return xor
        result = 0
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if xor(arr[i:j + 1]) == 0:
                    result += j - i
        return result
