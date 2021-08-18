class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def make(sorted_index_locations: [int]):
            jump_to_locations = [None] * N

            stack = []

            for index_location in sorted_index_locations:
                while stack and index_location > stack[-1]:
                    jump_to_locations[stack.pop()] = index_location
                stack.append(index_location)

            return jump_to_locations

        B = sorted(list(range(N)), key=lambda i: A[i])
        odd_jump_to_locations = make(B)
        B.sort(key=lambda i: -A[i])
        even_jump_to_locations = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if odd_jump_to_locations[i] is not None:
                odd[i] = even[odd_jump_to_locations[i]]
            if even_jump_to_locations[i] is not None:
                even[i] = odd[even_jump_to_locations[i]]

        return sum(odd)
