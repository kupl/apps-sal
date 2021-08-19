class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        np = [[0 for i in range(len(arr))] for j in range(2)]
        np[0][0] = 1 if arr[0] % 2 == 0 else 0
        np[1][0] = 1 if arr[0] % 2 == 1 else 0
        res = np[1][0]
        for i in range(1, len(arr)):
            if arr[i] % 2 == 0:
                np[0][i] = (1 + np[0][i - 1]) % 1000000007
                np[1][i] = np[1][i - 1] % 1000000007
            else:
                np[0][i] = np[1][i - 1] % 1000000007
                np[1][i] = (1 + np[0][i - 1]) % 1000000007
            res += np[1][i]
        return res % 1000000007
