class Solution:

    def splitArraySameAverage(self, A) -> bool:
        if sum(A) == 0 and len(A) > 1:
            return True
        elif len(A) == 1:
            return False
        mem = {}
        ss = sum(A)
        n = len(A)

        def rec(index, cur_sum, length):
            if cur_sum * (n - length) == length * (ss - cur_sum) and length > 0 and (length < n):
                return True
            elif index == n:
                return False
            elif (index, cur_sum) in mem:
                return mem[index, cur_sum]
            else:
                mem[index, cur_sum] = rec(index + 1, cur_sum + A[index], length + 1) | rec(index + 1, cur_sum, length)
                return mem[index, cur_sum]
        return rec(0, 0, 0)
