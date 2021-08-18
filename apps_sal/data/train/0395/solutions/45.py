class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:

        n = len(A)
        next_odd, next_even = [0] * n, [0] * n

        odd_stack = []
        for num, j in sorted([num, j] for j, num in enumerate(A)):
            while odd_stack and odd_stack[-1] < j:
                i = odd_stack.pop()
                next_odd[i] = j
            odd_stack.append(j)
        even_stack = []
        for num, j in sorted([-num, j] for j, num in enumerate(A)):
            while even_stack and even_stack[-1] < j:
                i = even_stack.pop()
                next_even[i] = j
            even_stack.append(j)

        odd, even = [0] * n, [0] * n

        odd[-1] = even[-1] = 1

        for i in range(n - 1)[::-1]:
            odd[i] = even[next_odd[i]]
            even[i] = odd[next_even[i]]

        return sum(odd)
