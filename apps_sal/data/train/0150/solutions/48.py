class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        disjoint = 0
        v = A[disjoint]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v:
                disjoint = i
                v = max_so_far
        return disjoint + 1
