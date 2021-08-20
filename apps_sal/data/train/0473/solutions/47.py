class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        for i in range(n - 1):
            x = arr[i]
            for j in range(i + 1, n):
                y = 0
                for k in range(j, n):
                    y = y ^ arr[k]
                    if x == y:
                        count += 1
                x = x ^ arr[j]
        return count
