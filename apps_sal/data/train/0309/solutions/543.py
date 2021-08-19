class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        mem = {}
        prev_values = set()
        for (idx, num) in enumerate(A):
            for pval in prev_values:
                diff = num - pval
                mem[num, diff] = max(mem.get((num, diff), 1), 1 + mem.get((pval, diff), 1))
            prev_values.add(num)
        return max(mem.values(), default=0)
