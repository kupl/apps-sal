class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        previous_less = [-1] * len(A)
        p_stack = []
        next_less = [len(A)] * len(A)
        n_stack = []
        for i in range(len(A)):
            n = A[i]
            while p_stack and A[p_stack[-1]] > n:
                p_stack.pop()
            if p_stack:
                previous_less[i] = p_stack[-1]
            else:
                previous_less[i] = -1
            p_stack.append(i)
            while n_stack and A[n_stack[-1]] > n:
                x = n_stack[-1]
                n_stack.pop()
                next_less[x] = i
            n_stack.append(i)
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(len(A)):
            left = i - previous_less[i]
            right = next_less[i] - i
            ans = (ans + A[i] * left * right) % mod
        return ans
