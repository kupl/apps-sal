class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:

        n = len(A)
        odd_jump = [-1] * n
        even_jump = [-1] * n

        final_odd = [False] * n
        final_even = [False] * n
        final_odd[-1] = True
        final_even[-1] = True

        stack = []
        for n, i in sorted((n, i) for i, n in enumerate(A)):
            while stack and stack[-1] < i:
                odd_jump[stack.pop()] = i
            stack.append(i)

        stack = []
        for n, i in sorted((-n, i) for i, n in enumerate(A)):
            while stack and stack[-1] < i:
                even_jump[stack.pop()] = i
            stack.append(i)

        for i in range(len(A) - 2, -1, -1):
            print(i)
            if odd_jump[i] != -1:
                final_odd[i] = final_even[odd_jump[i]]
            if even_jump[i] != -1:
                final_even[i] = final_odd[even_jump[i]]
        return sum(final_odd)
