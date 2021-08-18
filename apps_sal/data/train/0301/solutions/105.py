class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        A = [-1] + A
        B = [-1] + B

        dp_table = {}

        def helper(idx_a, idx_b):

            if (idx_a, idx_b) in dp_table:
                return dp_table[(idx_a, idx_b)]

            if idx_a == 0 or idx_b == 0:
                return 0

            elif A[idx_a] == B[idx_b]:

                dp_table[(idx_a, idx_b)] = helper(idx_a - 1, idx_b - 1) + 1
                return dp_table[(idx_a, idx_b)]
            else:
                dp_table[(idx_a, idx_b)] = max(helper(idx_a - 1, idx_b), helper(idx_a, idx_b - 1))
                return dp_table[(idx_a, idx_b)]

        return helper(len(A) - 1, len(B) - 1)
