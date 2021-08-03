class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n - 1):
            tmp = arr[i]
            for j in range(i + 1, n):
                tmp = tmp ^ arr[j]
                if tmp == 0:
                    res += j - i
        return res
