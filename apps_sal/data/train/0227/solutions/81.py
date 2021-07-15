class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros_indices = []
        for i in range(len(A)):
            if A[i] == 0:
                zeros_indices.append(i)

        longest_ones = 0


        longest_yet = 0
        for i in range(len(A)):
            if A[i] == 1:
                longest_yet += 1
                longest_ones = max(longest_ones, longest_yet)
            else:
                longest_yet = 0
        if K == 0:
            return longest_ones

        if K >= len(zeros_indices):
            return len(A)


        # [0, 1, 4, 5, 9, 12, 13, 14]
        zero_order = -1
        for i in range(len(A)):
            if A[i] == 0:
                zero_order += 1
                right_cons_ones = left_cons_ones = 0
                if zero_order + K < len(zeros_indices):
                    nxt = zero_order + K
                    right_cons_ones = zeros_indices[nxt] - zeros_indices[zero_order]
                else:
                    nxt = len(zeros_indices) - 1
                    right_cons_ones = zeros_indices[nxt] - zeros_indices[zero_order]
                    right_cons_ones += len(A) - zeros_indices[nxt]
                if not zero_order == 0:        
                    left_cons_ones = zeros_indices[zero_order] - zeros_indices[zero_order-1] - 1
                longest_ones = max(longest_ones, right_cons_ones + left_cons_ones)
        return longest_ones
