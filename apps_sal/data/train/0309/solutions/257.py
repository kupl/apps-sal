from collections import OrderedDict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # 1. Compute pairwise differences d_ij: O(n^2)
        #   [0 -5 -2 -7 1]
        #   [0  0  3 -2 6]
        #   [0  0  0 -5 3]
        #   [0  0  0  0 8]
        # 2. For each target node j in [1, n), record (diff, i) pairs where i in [0, n-1)
        # 3. For each target node j in [1, n), LAS[j][diff] = LAS[i].get(diff, 0) + 1
        # 4. Output max(LAS[n-1])
        diffs = {}
        for src in range(len(A) - 1):
            for tgt in range(len(A) - 1, src, -1):
                diff = A[tgt] - A[src]
                # Only record the closest j to maximize LAS
                diffs[src, diff] = tgt

        inbound_edges = {}
        for edge, tgt in diffs.items():
            inbound_edges.setdefault(tgt, []).append(edge)

        max_length = 0
        memo = {0: {}}
        for tgt in range(1, len(A)):
            memo[tgt] = {}
            for src, diff in inbound_edges[tgt]:
                seq_length = memo[src].get(diff, 1) + 1
                if seq_length > memo[tgt].get(diff, 0):
                    memo[tgt][diff] = seq_length
                    max_length = max(seq_length, max_length)

        return max_length
