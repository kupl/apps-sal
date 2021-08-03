class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        mark = [{}]
        res = 0

        for i in range(1, n):
            mark.append({})
            for j in range(i):
                delta = A[i] - A[j]
                if delta in mark[j]:
                    if delta in mark[i]:
                        mark[i][delta] = max(mark[j][delta] + 1, mark[i][delta])
                    else:
                        mark[i][delta] = mark[j][delta] + 1
                else:
                    if delta not in mark[i]:
                        mark[i][delta] = 1

                if mark[i][delta] > res:
                    res = mark[i][delta]

        return res + 1
