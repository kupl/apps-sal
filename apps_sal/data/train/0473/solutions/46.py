class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        out = 0
        for i in range(n - 1):
            a = arr[i]
            for j in range(i + 1, n):
                b = 0
                for k in range(j, n):
                    b ^= arr[k]
                    if a == b:
                        out += 1
                a ^= arr[j]

        return out
