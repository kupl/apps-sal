class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        (ans, n) = (0, len(arr))
        xors = [0] * (n + 1)
        for i in range(1, n + 1):
            xors[i] = xors[i - 1] ^ arr[i - 1]
        for i in range(n):
            for k in range(i + 1, n):
                if xors[k + 1] ^ xors[i] != 0:
                    continue
                for j in range(i + 1, k + 1):
                    if xors[j] ^ xors[i] == xors[k + 1] ^ xors[j]:
                        ans += 1
        return ans
