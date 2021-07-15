class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr) - 1):
            accu = arr[i]
            for k in range(i + 1, len(arr)):
                accu ^= arr[k]
                if not accu:
                    res += k - i
        return res
