class Solution:

    def clumsy(self, N: int) -> int:
        op = ['*', '//', '+', '-']
        op_idx = -1
        idx = N
        result = str(N)
        while idx > 1:
            idx -= 1
            op_idx = (op_idx + 1) % 4
            result += op[op_idx] + str(idx)
        return eval(result)
