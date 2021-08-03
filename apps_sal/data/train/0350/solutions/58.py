from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        total = 0
        l1 = 0
        l2 = 0
        memo1 = defaultdict(int)
        memo2 = defaultdict(int)

        for r, c in enumerate(A):

            memo1[c] += 1
            memo2[c] += 1

            while(len(memo1) > K):
                memo1[A[l1]] -= 1
                if(memo1[A[l1]] == 0):
                    del memo1[A[l1]]
                l1 += 1

            while(len(memo2) >= K):
                memo2[A[l2]] -= 1
                if(memo2[A[l2]] == 0):
                    del memo2[A[l2]]
                l2 += 1

            total += l2 - l1

        return total
