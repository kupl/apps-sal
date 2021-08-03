class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        s, memo = set(A), {}
        for i in range(len(A)):
            for j in range(i):
                if (A[i] - A[j]) in s and (A[i] - A[j]) < A[j]:
                    memo[A[j], A[i]] = memo.get((A[i] - A[j], A[j]), 2) + 1
        return max(memo.values() or [0])
