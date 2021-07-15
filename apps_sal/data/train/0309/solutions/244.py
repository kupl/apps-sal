from collections import defaultdict
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # 3, 6, 9, 12
        # 1,3 -> 0
        # 2,6 -> 0
        # 2,3 -> 1
        # 3,9 -> 0
        # 3,6 -> 1
        # 3,3 -> 2
        count = 2
        diff_map = defaultdict(dict)
        for i in range(len(A)):
            for j in range(0, i):
                #print(i, j, diff_map[i])
                diff = A[i] - A[j]
                diff_map[i][diff] = 1 + diff_map[j].get(diff, 1)
                count = max(count, diff_map[i][diff])
        return count

