class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xor = [0 for i in range(n + 1)]
        for i in range(n):
            xor[i + 1] = xor[i] ^ arr[i]

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if xor[i] ^ xor[j] == xor[j] ^ xor[k + 1]:
                        ans += 1
        return ans
