class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result_set = set()
        results = set()
        for num in A:
            results = {j | num for j in results}
            results.add(num)
            result_set.update(results)
        return len(result_set)
