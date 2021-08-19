class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:

        n = len(A)
        # build arrays to store the destination of current idx
        next_odd, next_even = [0] * n, [0] * n

        # store legal next index j if odd_jump
        odd_stack = []
        # sort smallest value, then smallest index
        # we want to find the min-larger
        for num, j in sorted([num, j] for j, num in enumerate(A)):
            while odd_stack and odd_stack[-1] < j:  # i < j
                i = odd_stack.pop()
                next_odd[i] = j
            odd_stack.append(j)
        # store legal nect index j if even_jump
        even_stack = []
        # sort max value, then smallest index
        # we want to find the max-smaller
        for num, j in sorted([-num, j] for j, num in enumerate(A)):
            while even_stack and even_stack[-1] < j:
                i = even_stack.pop()
                next_even[i] = j
            even_stack.append(j)

        # store if odd/even_jumps leads to the last idx
        # trace back from last one = > base case: always true
        odd, even = [0] * n, [0] * n
        odd[-1] = even[-1] = 1

        for i in range(n - 1)[::-1]:
            # consider an odd_jump, then next one must be even
            # use next_odd[i] to find the idx j after jump from i
            # use indx j for even_jump, if even[j] is true, odd[i] is true as well
            odd[i] = even[next_odd[i]]
            even[i] = odd[next_even[i]]

        # must start with odd(first jump)
        return sum(odd)
