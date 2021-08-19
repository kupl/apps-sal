class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            a = arr[i]
            for j in range(i + 1, len(arr)):
                a = a ^ arr[j]
                b = arr[j]
                for k in range(j, len(arr)):
                    b = b ^ arr[k]
                    if a == b:
                        count += 1
        return count
