class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        num_count = len(A)
        previous_best = [0] * num_count
        current_best = [0] * num_count

        previous_best[0] = A[0]
        for index in range(1, num_count):
            A[index] += A[index - 1]
            previous_best[index] = A[index] / (index + 1)

        for partition_count in range(1, K):
            for end_index in range(partition_count, num_count - K + partition_count + 1):

                current_best[end_index] = max(
                    (A[end_index] - A[start_index]) / (end_index - start_index) + previous_best[start_index]
                    for start_index in range(partition_count - 1, end_index)
                )
            current_best, previous_best = previous_best, current_best
        return previous_best[-1]
