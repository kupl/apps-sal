class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n):
            arr[i] ^= arr[i - 1]
        out = 0
        for i in range(n):
            if arr[i] == 0:
                out += i
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    out += j - i - 1
        return out
