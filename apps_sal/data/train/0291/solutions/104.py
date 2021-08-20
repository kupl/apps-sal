class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        (odd, even) = ([0] * n, [0] * n)
        for (i, v) in enumerate(arr):
            if not i:
                odd[i] += v % 2 == 1
                even[i] += v % 2 != 1
            elif v % 2:
                odd[i] += 1 + even[i - 1]
                even[i] += odd[i - 1]
            else:
                odd[i] += odd[i - 1]
                even[i] += 1 + even[i - 1]
        return sum(odd) % (10 ** 9 + 7)
