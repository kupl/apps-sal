class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        best_of_prev = A[0] - 1
        maximum = 0

        for spot in A[1:]:
            if spot + best_of_prev > maximum:
                maximum = spot + best_of_prev

            if spot > best_of_prev:
                best_of_prev = spot

            best_of_prev -= 1

        return maximum
