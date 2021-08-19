class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        r = 0
        max_count = K
        while l < len(A) and r < len(A):
            while r < len(A):
                if A[r] == 1:
                    r += 1
                elif K > 0:
                    r += 1
                    K -= 1
                else:
                    break
            if r - l + 1 > max_count:
                max_count = r - l
            print(l, r, max_count)
            if A[l] == 0:
                K += 1
            l += 1
        return max_count
