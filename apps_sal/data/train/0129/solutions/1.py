class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        result = 0
        current = A[0]
        current_pos = 0
        for i in range(1, len(A)):
            value = current + A[i] + current_pos - i
            if value > result:
                result = value
            if current <= A[i] + i - current_pos:
                current = A[i]
                current_pos = i

        return result
