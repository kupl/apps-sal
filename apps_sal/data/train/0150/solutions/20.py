class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        split_index = 0
        local_max = A[0]
        max_num = local_max
        for i in range(len(A)):
            if A[i] < local_max:
                split_index = i
                local_max = max_num
            else:
                max_num = max(max_num, A[i])
        return split_index + 1
