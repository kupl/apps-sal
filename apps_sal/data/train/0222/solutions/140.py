class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # Create a hashmap to find index from value
        val_to_idx = {val: idx for idx, val in enumerate(A)}

        def maxLevel(A: List[int], sum_idx: int, var2_idx: int, level: int) -> int:
            if var2_idx == 0:
                return level
            # print(f\"In maxLevel: sum={A[sum_idx]} (index={sum_idx}), var2={A[var2_idx]} (index={var2_idx}), level={level}\")
            val_to_search = A[sum_idx] - A[var2_idx]
            returned_idx = val_to_idx.get(val_to_search, None)
            if returned_idx is not None and returned_idx < var2_idx:
                # print(f\"Found value at index: {returned_idx}\")
                return maxLevel(A, var2_idx, returned_idx, level + 1)
            # print(f\"Index not found, returning level: {level}\")
            return level

        longest = 0
        for i in reversed(list(range(len(A)))):
            for j in reversed(list(range(i))):
                result_length = maxLevel(A, i, j, 2)
                longest = max(longest, result_length)

        if longest < 3:
            return 0
        return longest
