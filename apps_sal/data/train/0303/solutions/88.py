class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        M = [0 for i in range(len(arr))]

        M[0] = arr[0]

        # if len(arr) > 1:
        #    M[1] = max(arr[0],arr[1]) * 2

        # if len(arr) > 2:
        #    M[2] = max(arr[0],arr[1],arr[2]) * 3

        for i in range(1, len(arr)):

            if i < k:
                M[i] = max(arr[:i + 1]) * (i + 1)

            for j in range(1, min(k + 1, i + 1)):

                M[i] = max(M[i], M[i - j] + max(arr[i - j + 1:i + 1]) * j)

        # print(M)

        return M[-1]
