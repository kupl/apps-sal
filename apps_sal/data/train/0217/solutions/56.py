from typing import List, Set


class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        all_results: Set[int] = set()
        prev_results: Set[int] = set()
        for start_index in range(len(A)):
            curr_results: Set[int] = set()
            curr_results.add(A[start_index])
            for prev_result in prev_results:
                curr_results.add(prev_result | A[start_index])
            all_results |= curr_results
            prev_results = curr_results
        return len(all_results)
