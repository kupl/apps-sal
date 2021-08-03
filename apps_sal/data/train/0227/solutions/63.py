class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        count_1 = 0
        zero_inx = []
        res = 0
        zero_before = -1
        for i in range(len(A)):
            if A[i] == 1:
                count_1 += 1
            else:
                zero_inx.append(i)
                if K > 0:
                    K -= 1
                    count_1 += 1
                elif K == 0:
                    res = max(res, count_1)
                    first_0 = zero_inx.pop(0)
                    count_1 -= (first_0 - zero_before - 1)
                    zero_before = first_0
        res = max(res, count_1)
        return res
