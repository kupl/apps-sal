from collections import deque
from bisect import bisect_left
from math import inf


def calc_jumps(nums):
    nums = sorted((a, i) for i, a in enumerate(nums))
    jumps = [None] * len(nums)
    index_stack = deque([inf])
    for a, i in reversed(nums):
        jumps[i] = index_stack[bisect_left(index_stack, i)]
        while index_stack and index_stack[0] <= i:
            index_stack.popleft()
        index_stack.appendleft(i)
    return jumps


class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        odd_jumps = calc_jumps(A)
        even_jumps = calc_jumps([-a for a in A])
        odd_start_goodness = [i + 1 == len(A) for i in range(len(A))]
        even_start_goodness = [i + 1 == len(A) for i in range(len(A))]
        for i in reversed(range(len(A) - 1)):
            if odd_jumps[i] != inf:
                odd_start_goodness[i] = even_start_goodness[odd_jumps[i]]
            if even_jumps[i] != inf:
                even_start_goodness[i] = odd_start_goodness[even_jumps[i]]
        return sum(odd_start_goodness)
