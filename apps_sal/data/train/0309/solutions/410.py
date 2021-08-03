from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        A_indices = defaultdict(list)
        for i, a in enumerate(A):
            A_indices[a].append(i)
        lengths = defaultdict(lambda: 2)
        best = 2

        for i in range(len(A) - 3, -1, -1):
            for j in range(i + 1, len(A) - 1):
                if 2 * A[j] - A[i] in A_indices:
                    indices = A_indices[2 * A[j] - A[i]]
                    # find earliest occurrence of 2 * A[j] + A[i] after j
                    if indices[-1] <= j:
                        continue
                    if indices[0] > j:
                        r = 0
                    else:
                        l = 0
                        r = len(indices) - 1
                        while l < r - 1:
                            mid = (l + r) // 2
                            if indices[mid] <= j:
                                l = mid
                            else:
                                r = mid
                    lengths[i, j] = 1 + lengths[j, indices[r]]
                    best = max(best, lengths[i, j])
        return best
