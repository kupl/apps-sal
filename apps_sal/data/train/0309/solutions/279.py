from typing import Dict, Tuple


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n: int = len(A)
        dp: Dict[Tuple[int, int], int] = {}
        answer: int = 0
        for i in range(n):
            for j in range(i + 1, n):
                diff: int = A[j] - A[i]
                length: int = dp.get((i, diff), 1) + 1
                dp[j, diff] = length
                answer = max(answer, length)
        return answer
