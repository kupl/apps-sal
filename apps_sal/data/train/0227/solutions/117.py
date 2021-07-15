class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        le = 0
        for ri in range(len(A)):
            K -= (1-A[ri]) # 如果A[ri]是0, k 要减去1
            
            print (le, ri)
            if K < 0:
                K += (1 - A[le])
                le += 1
        return ri - le + 1
