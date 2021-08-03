class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        MOD = int(1e9 + 7)
        even, odd = [0] * (n + 1), [0] * (n + 1)
        for i, a in enumerate(arr):
            if a % 2 == 1:
                even[i] = odd[i - 1]
                odd[i] = (even[i - 1] + 1)
            else:
                even[i] = (even[i - 1] + 1)
                odd[i] = odd[i - 1]

        return sum(odd) % MOD
