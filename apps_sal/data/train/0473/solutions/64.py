class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        xor = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if j == i:
                    xor[i][j] = arr[j]
                else:
                    xor[i][j] = xor[i][j - 1] ^ arr[j]
        ans = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                for k in range(j, len(arr)):
                    if xor[i][j - 1] == xor[j][k]:
                        ans += 1
        return ans
