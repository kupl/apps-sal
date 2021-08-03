class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        my_set = [set([A[i]]) for i in range(len(A))]

        for i in range(1, len(A)):
            for prev_result in my_set[i - 1]:
                my_set[i].add(A[i] | prev_result)

        return len(set.union(*my_set))
