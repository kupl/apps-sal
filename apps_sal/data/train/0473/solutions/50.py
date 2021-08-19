class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for k in range(len(arr)):
            b = 0
            for j in range(k, 0, -1):
                b = b ^ arr[j]
                a = 0
                for i in range(j - 1, -1, -1):
                    a = a ^ arr[i]
                    if a == b:
                        count += 1
        return count
