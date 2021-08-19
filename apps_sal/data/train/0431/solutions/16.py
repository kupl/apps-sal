class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        (n, mod) = (len(A), 10 ** 9 + 7)
        (left, right, stack1, stack2) = ([0] * n, [0] * n, [], [])
        for i in range(n):
            count = 1
            while stack1 and stack1[-1][0] > A[i]:
                count += stack1.pop()[1]
            left[i] = count
            stack1.append([A[i], count])
        for i in range(n - 1, -1, -1):
            count = 1
            while stack2 and stack2[-1][0] >= A[i]:
                count += stack2.pop()[1]
            right[i] = count
            stack2.append([A[i], count])
        return sum((a * l * r for (a, l, r) in zip(A, left, right))) % mod
