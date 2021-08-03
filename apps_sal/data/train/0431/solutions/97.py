class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        prev_stack = []
        next_stack = []

        prev_smaller = []
        next_smaller = []

        for i in range(len(A)):
            prev_smaller.append(i)
            next_smaller.append(len(A) - i - 1)

        for i in range(len(A)):
            while len(next_stack) > 0 and A[next_stack[-1]] >= A[i]:
                idx = next_stack.pop()
                next_smaller[idx] = i - idx - 1

            next_stack.append(i)

        for i in range(len(A) - 1, -1, -1):
            while len(prev_stack) > 0 and A[prev_stack[-1]] > A[i]:
                idx = prev_stack.pop()
                prev_smaller[idx] = idx - i - 1

            prev_stack.append(i)

        m = 10 ** 9 + 7
        result = 0
        for i in range(len(A)):
            num_occurrences = (prev_smaller[i] + 1) * (next_smaller[i] + 1)
            result = (result + num_occurrences * A[i]) % m

        return result
