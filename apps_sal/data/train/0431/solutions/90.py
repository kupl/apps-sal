class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        left = self.first_left_smallest(A)
        right = self.first_right_smallest(A)
        count = 0
        MOD = 10 ** 9 + 7
        for i in range(n):
            l = left[i] if left[i] != None else -1
            r = right[i] if right[i] != None else n
            n1 = i - l - 1
            n2 = r - i - 1
            num_of_sub = (n1 + 1) * (n2 + 1)
            print((i, num_of_sub))
            count += A[i] * num_of_sub
        return count % MOD

    def first_left_smallest(self, A):
        n = len(A)
        stack = []
        res = [None] * n
        for i in range(n - 1, -1, -1):
            while stack and A[i] <= A[stack[-1]]:
                j = stack.pop()
                res[j] = i
            stack.append(i)
        return res

    def first_right_smallest(self, A):
        n = len(A)
        stack = []
        res = [None] * n
        for i in range(n):
            while stack and A[i] < A[stack[-1]]:
                j = stack.pop()
                res[j] = i
            stack.append(i)
        return res

    def brute_force(self, A):
        n = len(A)
        s = 0
        for i in range(n):
            smallest = float('inf')
            for j in range(i, n):
                smallest = min(smallest, A[j])
                s += smallest
        return s % (10 ** 9 + 7)
