class Solution:

    def subarrayBitwiseORs(self, A):
        tabulation = [set([A[i]]) for i in range(len(A))]
        for i in range(1, len(A)):
            for previous_result in tabulation[i - 1]:
                tabulation[i].add(A[i] | previous_result)
        return len(set.union(*tabulation)) if len(A) > 0 else 0
