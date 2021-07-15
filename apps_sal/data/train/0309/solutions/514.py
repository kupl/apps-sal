from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        def calc(A):
            memo = [dict() for _ in range(len(A))]
            ret = 1
            for i in range(len(A) - 1, -1, -1):
                for j in range(i + 1, len(A)):
                    if A[j] < A[i]:
                        continue
                    diff = A[j] - A[i]
                    memo[i][diff] = max(memo[i].get(diff, 0), memo[j].get(diff, 1) + 1)
                    ret = max(ret, memo[i][diff])
            return ret
        
        return max(
            calc(A), calc(list(reversed(A)))
        )
