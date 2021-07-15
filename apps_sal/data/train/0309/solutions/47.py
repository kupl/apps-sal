from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # mapping: idx -> (mapping: arithmetic_step -> longest_arithmetic_subsequence_with_this_step_ending_at_idx
        d = defaultdict(lambda: defaultdict(lambda: 1))
        
        for i,a in enumerate(A):
            # LAS: A[i]
            d[i][0] = 1
            for j in range(i):
                # Consider each subsequence that ends at i ~        A[?] ... A[??] A[j] A[i]
                # A[i] - A[j] denotes the step
                # LSA(j, step) := length of LSA ending at j with progression equal to step
                # We only care about count, not the actual sequence, so length of such subsequence will be: 1 + LSA(j, step)
                step = A[i] - A[j]
                d[i][step] = d[j][step] + 1
        return max([max(dn.values()) for dn in d.values()])
