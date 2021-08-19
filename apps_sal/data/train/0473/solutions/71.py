class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                target = arr[j - 1]
                if i > 0:
                    target ^= arr[i - 1]
                for k in range(j, len(arr)):
                    curr = arr[k]
                    curr ^= arr[j - 1]
                    if curr == target:
                        count += 1
        return count
