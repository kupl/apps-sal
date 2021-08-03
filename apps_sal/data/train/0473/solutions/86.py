class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        c = 0
        xor = 0
        for i in range(n - 1):
            xor = arr[i]
            for j in range(i + 1, n):
                xor ^= arr[j]
                if xor == 0:
                    c += (j - i)
        return c
