class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if i:
                        a = arr[j - 1] ^ arr[i - 1]
                    else:
                        a = arr[j - 1]
                    b = arr[k] ^ arr[j - 1]
                    if a == b:
                        res += 1
        return res
