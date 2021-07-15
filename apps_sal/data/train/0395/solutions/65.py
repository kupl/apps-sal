class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)
        # returns a list of the index you can jump to from any index in A
        # runs twice since where you jump to on an even jump is diff than an odd jump
        def make(sorted_index_locations: [int]):
            # 'None' means no jump is possible from this index in A
            jump_to_locations = [None] * N

            # The stack is used to track indexes that you
            stack = []

            # now walk the list in order
            # if index_location > stack[-1], it means index_location is past stack[-1]
            # since sorted_index_locations is sorted smallest to largest, all smaller numbers are behind it
            # so it's finding the next-lowest number that's further up the list -- this is where it will jump to.

            for index_location in sorted_index_locations:
                while stack and index_location > stack[-1]:
                    # all items on the stack are smaller and are behind it in A
                    # so they'll jump to the same place this index will jump to
                    jump_to_locations[stack.pop()] = index_location
                # if stack is empty or this index is higher than the last on on the stack,
                # push this onto the stack and go to the next index
                stack.append(index_location)

            # jump_to_locations contains the location you jump, or None if you can't jump from that index
            return jump_to_locations

        B = sorted(list(range(N)), key=lambda i: A[i])
        odd_jump_to_locations = make(B)
        B.sort(key=lambda i: -A[i])
        even_jump_to_locations = make(B)

        # odd and even have 'good indexes' where they end up True after this.
        # initialize assuming only that the very last location (A[N-1]) will always be True.
        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True

        for i in range(N - 2, -1, -1):
            if odd_jump_to_locations[i] is not None:
                odd[i] = even[odd_jump_to_locations[i]]
            if even_jump_to_locations[i] is not None:
                even[i] = odd[even_jump_to_locations[i]]

        return sum(odd)


