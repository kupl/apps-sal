import sys


class Solution:

    def is_overlap(self, i, j, L, M):
        if len(set(range(i, i + L)) & set(range(j, j + M))) > 0:
            return True
        else:
            return False

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        max_two_sum = 0
        N = len(A)

        def maxOverlap(arr: List[int]) -> int:
            n = len(arr)
            if n < L:
                return -1
            roll_max = 0

            for i in range(L):
                roll_max += arr[i]
            curr_max = roll_max

            start = 0
            for n in arr[L:]:
                roll_max = roll_max - arr[start] + n
                curr_max = max(curr_max, roll_max)
                start += 1
            return curr_max

        for x in range(N):
            curr_total = sum(A[x:x + M])
            first_half = maxOverlap(A[:x])
            second_half = maxOverlap(A[x + M:])
            max_two_sum = max(max_two_sum, curr_total + first_half, curr_total + second_half)

        return max_two_sum
