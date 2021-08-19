class Solution:
    def minSwap(self, A, B):
        # 这道题是说A和B的swap是相对应的位置swap
        # index的遍历是同时遍历A和B的

        # 状态就是当前处理的是第几位 + 这一位是不是swap过来的
        #                 start^       swapped^
        return self._dfs(A, B, start=0, swapped=False, memo={})

    def _dfs(self, A, B, start, swapped, memo):
        if start == len(A):
            return 0

        key = (start, swapped)
        if key in memo:
            return memo[key]

        res = 2 ** 31 - 1
        prev_a = A[start - 1] if start > 0 else -2 ** 31 - 1
        prev_b = B[start - 1] if start > 0 else -2 ** 31 - 1

        if A[start] > prev_a and B[start] > prev_b:
            res = min(res, self._dfs(A, B, start + 1, False, memo))

        # 注意这里不能跳过
        # 否则会漏掉一些case
        if A[start] > prev_b and B[start] > prev_a:
            A[start], B[start] = B[start], A[start]
            res = min(res, self._dfs(A, B, start + 1, True, memo) + 1)
            A[start], B[start] = B[start], A[start]

        memo[key] = res
        return res
