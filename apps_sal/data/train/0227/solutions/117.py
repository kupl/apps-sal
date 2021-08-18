class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        le = 0
        for ri in range(len(A)):
            K -= (1 - A[ri])

            print(le, ri)
            if K < 0:
                K += (1 - A[le])
                le += 1
        return ri - le + 1
