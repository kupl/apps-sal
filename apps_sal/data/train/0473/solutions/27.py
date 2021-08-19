class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        arr = [0] + arr
        res = 0
        for k in range(1, len(arr)):
            arr[k] ^= arr[k - 1]
            for i in range(1, k):
                if arr[k] ^ arr[i - 1] == 0:
                    res += k - i
        return res
