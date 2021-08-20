class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        if len(arr) < 2:
            return count
        for i in range(len(arr)):
            a = 0
            for j in range(i, len(arr) - 1):
                a ^= arr[j]
                b = 0
                for k in range(j + 1, len(arr)):
                    b ^= arr[k]
                    if a == b:
                        count += 1
        return count
