import collections


class Solution:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        count = collections.Counter()
        for (i, rowa) in enumerate(A):
            for j in range(len(rowa)):
                if rowa[j]:
                    for (m, rowb) in enumerate(B):
                        for n in range(len(rowb)):
                            if rowb[n]:
                                count[i - m, j - n] += 1
        return max(list(count.values()) or [0])
