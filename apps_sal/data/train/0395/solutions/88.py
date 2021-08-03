class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        '''
        Algorithm
        ---------
        We need to jump alternatively higher and lower until we reach the end of the array.
        '''

        stack = []

        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        for _, i in sorted([val, index] for index, val in enumerate(A)):
            # Check if the index at the top of the stack
            # is less than the current index i. If it is
            # then the current index i is the next greater element for the index at the top of the stack
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for _, i in sorted([-val, index] for index, val in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n

        # increment the last index in both the lower and higher
        # since we know that the end of the array can be reached from the
        # last index
        higher[-1] += 1
        lower[-1] += 1

        for i in reversed(list(range(n - 1))):
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)
