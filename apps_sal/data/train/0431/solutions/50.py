from queue import deque
from collections import defaultdict


class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        A = [float('-inf')] + A + [float('-inf')]
        left = deque()
        left.append(0)
        right = deque()
        right.appendleft(len(A) - 1)
        left_b = defaultdict(int)
        right_b = defaultdict(int)
        for i in range(1, len(A) - 1):
            while left and A[left[-1]] > A[i]:
                left.pop()
            left_b[i] = left[-1] + 1
            left.append(i)
        for i in reversed(range(1, len(A) - 1)):
            while right and A[right[0]] >= A[i]:
                right.popleft()
            right_b[i] = right[0] - 1
            right.appendleft(i)
        res = 0
        for i in range(1, len(A) - 1):
            res += (i - left_b[i] + 1) * (right_b[i] - i + 1) * A[i]
        return res % (10 ** 9 + 7)
