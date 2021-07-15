class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count, n = 0, len(arr)
        for i in range(n - 1):
            accu = arr[i]
            for k in range(i + 1, n):
                accu ^= arr[k]
                if accu == 0: count += k - i
        return count
