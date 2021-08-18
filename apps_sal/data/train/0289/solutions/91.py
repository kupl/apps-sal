class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L + M > len(A):
            return 0
        answer = [0]
        max_sum = -float('inf')
        for i in range(len(A)):
            answer.append(answer[-1] + A[i])
        for i in range(len(A) - L + 1):
            if i >= M:
                for j in range(i - M + 1):
                    max_sum = max(max_sum, answer[i + L] - answer[i] + answer[j + M] - answer[j])
            if i + L <= len(A) - M:
                for j in range(i + L, len(A) - M + 1):
                    max_sum = max(max_sum, answer[i + L] - answer[i] + answer[j + M] - answer[j])

        return max_sum
