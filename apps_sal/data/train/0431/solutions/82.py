class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        l_large = [0] * n
        l_stack = [(A[0], 0)]
        r_large = [0] * n
        r_stack = [(A[n - 1], n - 1)]
        for i in range(1, n):
            while l_stack and A[i] <= l_stack[-1][0]:
                (_, idx) = l_stack.pop()
                l_large[i] = max(l_large[i], i - idx + l_large[idx])
            else:
                l_stack.append((A[i], i))
            while r_stack and A[n - i - 1] < r_stack[-1][0]:
                (_, idx) = r_stack.pop()
                r_large[n - i - 1] = max(r_large[n - i - 1], idx - (n - i - 1) + r_large[idx])
            else:
                r_stack.append((A[n - i - 1], n - i - 1))
        return sum(((1 + l_large[i] + r_large[i] + l_large[i] * r_large[i]) * A[i] for i in range(n))) % int(1000000007)
