class Solution:

    def partitionDisjoint(self, A: List[int]) -> int:
        i = 1
        l_max = A[i - 1]
        r_min = min(A[i:])
        while l_max > r_min:
            i += 1
            l_max = max(l_max, A[i - 1])
            if A[i - 1] == r_min:
                r_min = min(A[i:])
        return i
