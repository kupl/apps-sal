class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        (ans, n) = (0, len(arr))
        xors = [0] * (n + 1)
        for i in range(1, n + 1):
            xors[i] = xors[i - 1] ^ arr[i - 1]
        for i in range(n):
            for j in range(i + 1, n):
                a = xors[j] ^ xors[i]
                for k in range(j, n):
                    if a == xors[k + 1] ^ xors[j]:
                        ans += 1
        return ans
