class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        start = arr[0]
        res = 0
        for i in range(1, len(arr)):
            start ^= arr[i]
            arr[i] = start
        arr = [0] + arr
        for i in range(1, len(arr)):
            for j in range(i + 1, len(arr)):
                first_part = arr[j - 1] ^ arr[i - 1]
                for k in range(j, len(arr)):
                    second_part = arr[k] ^ arr[j - 1]
                    if first_part == second_part:
                        res += 1
        return res
