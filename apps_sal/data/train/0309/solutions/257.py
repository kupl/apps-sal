from collections import OrderedDict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        diffs = {}
        for src in range(len(A) - 1):
            for tgt in range(len(A) - 1, src, -1):
                diff = A[tgt] - A[src]
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
