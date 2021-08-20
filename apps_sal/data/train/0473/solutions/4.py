class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        xors = [0] * (n + 1)
        for z in range(n):
            xors[z] = xors[z - 1] ^ arr[z]
        for i in range(n - 1):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = xors[j - 1] ^ xors[i - 1]
                    b = xors[k] ^ xors[j - 1]
                    if a == b:
                        res += 1
        return res
