class Solution:

    def _identify_limit(self, A, current_limit, K, char_count_after_limit):
        temp_char = A[current_limit]
        while char_count_after_limit.get(temp_char, 0) > 1:
            char_count_after_limit[temp_char] = char_count_after_limit[temp_char] - 1
            current_limit += 1
            temp_char = A[current_limit]
        return (current_limit, char_count_after_limit)

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        char_info = {item: [] for item in set(A)}
        unique_char_count = {}
        unique_char = set()
        start_idx = 0
        end_idx = 0
        num_substr = 0
        current_subarray = []
        current_valid_count = 0
        limit_idx = 0
        while end_idx < len(A) + 1:
            if len(unique_char_count) == K:
                (limit_idx, unique_char_count) = self._identify_limit(A, limit_idx, K, unique_char_count)
                num_substr += limit_idx - start_idx + 1
                if end_idx < len(A):
                    current_char = A[end_idx]
                    unique_char_count[current_char] = unique_char_count.get(current_char, 0) + 1
                end_idx += 1
            elif len(unique_char_count) > K:
                current_char = A[limit_idx]
                unique_char_count.pop(current_char)
                start_idx = limit_idx + 1
                limit_idx = start_idx
            else:
                if end_idx < len(A):
                    current_char = A[end_idx]
                    unique_char_count[current_char] = unique_char_count.get(current_char, 0) + 1
                end_idx += 1
        return num_substr
