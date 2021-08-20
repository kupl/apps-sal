class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        even = [0] * n
        odd = [0] * n
        for (i, x) in enumerate(arr):
            if i == 0:
                if x % 2 == 0:
                    even[i] = 1
                else:
                    odd[i] = 1
            elif x % 2 == 0:
                even[i] = even[i - 1] + 1
                odd[i] = odd[i - 1]
            else:
                even[i] = odd[i - 1]
                odd[i] = even[i - 1] + 1
        return sum(odd) % (int(1000000000.0) + 7)
