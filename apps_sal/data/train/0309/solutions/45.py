from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        """
        # Note:
            A.length >= 2
        # Analysis:
            Arithmetic sequence

        """
        n = len(A)
        res = 2
        dif_arr = [defaultdict(int) for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                dif = A[i] - A[j]
                if dif in dif_arr[j]:
                    dif_arr[i][dif] = dif_arr[j][dif] + 1
                    res = max(res, dif_arr[i][dif] + 1)
                else:
                    dif_arr[i][dif] = 1
        return res
