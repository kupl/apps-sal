class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        l = len(arr)
        count = 0
        for k in range(1, l):
            b = 0
            for j in range(k, 0, -1):
                b ^= arr[j]
                a = 0
                for i in range(j - 1, -1, -1):
                    a ^= arr[i]
                    if a == b:
                        count += 1
        return count
