class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # for each array of length L we need to find the max sum array of length M
        # we keep an array of cummulative sum so that we do not need to calculate them again and again
        if L + M > len(A):
            # no such array is possible
            return 0
        answer = [0]
        max_sum = -float('inf')
        for i in range(len(A)):
            answer.append(answer[-1] + A[i])
        for i in range(len(A) - L + 1):
            if i >= M:
                # then only we can find non overlapping subarray in the beginning
                for j in range(i - M + 1):
                    # print(i,j, answer[i+L] - answer[i], answer[j+M] - answer[j])
                    max_sum = max(max_sum, answer[i + L] - answer[i] + answer[j + M] - answer[j])
            if i + L <= len(A) - M:
                # then only we can find non overlapping subarray in the end
                for j in range(i + L, len(A) - M + 1):
                    # print(i,j,answer[i+L] - answer[i], answer[j+M] - answer[j])
                    max_sum = max(max_sum, answer[i + L] - answer[i] + answer[j + M] - answer[j])

        return max_sum
