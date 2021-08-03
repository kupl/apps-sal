class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def get_op(n):
            op_0 = 0
            op_1 = 0
            while n != 0:
                if n % 2 == 0:
                    op_1 += 1
                    n = n // 2
                else:
                    op_0 += 1
                    n -= 1
            return op_0, op_1

        ans = 0
        op_1 = 0
        for n in nums:
            tmp_0, tmp_1 = get_op(n)
            ans += tmp_0
            op_1 = max(op_1, tmp_1)
        return ans + op_1
