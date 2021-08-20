class Solution:

    def maxWidthRamp(self, A: List[int]) -> int:
        sorted_indices = sorted(list(range(len(A))), key=lambda x: A[x])
        minimum_index = sorted_indices[0]
        answer = 0
        for i in range(1, len(sorted_indices)):
            if sorted_indices[i] > minimum_index:
                answer = max(answer, sorted_indices[i] - minimum_index)
            else:
                minimum_index = sorted_indices[i]
        return answer
