class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        pre_stack = []
        pre_val = [-1] * n
        for i, a in enumerate(A):
            while pre_stack and A[pre_stack[-1]] >= a:
                pre_stack.pop()
            if pre_stack:
                pre_val[i] = pre_stack[-1] + 1
            else:
                pre_val[i] = 0
            pre_stack.append(i)

        post_stack = []
        post_val = [-1] * n
        for i in range(n - 1, -1, -1):
            while post_stack and A[post_stack[-1]] > A[i]:
                post_stack.pop()
            if post_stack:
                post_val[i] = post_stack[-1] - 1
            else:
                post_val[i] = n - 1
            post_stack.append(i)

        # print(pre_val)
        # print(post_val)

        ans = 0
        mod_cst = 10**9 + 7
        for i in range(n):
            ans += (i - pre_val[i] + 1) * (post_val[i] - i + 1) * A[i]
            ans %= mod_cst
        return ans
