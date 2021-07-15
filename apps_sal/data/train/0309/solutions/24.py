class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A)<2: return len(A)
        table = []
        result = 1
        
        for i, z in enumerate(A):
            table.append(collections.defaultdict(lambda: 1))
            for j in range(i):
                diff = z - A[j]
                table[i][diff] = table[j][diff] + 1
                #if table[i][diff] > result: result = table[i][diff]
        
        return max([max(y.values()) for y in table])
