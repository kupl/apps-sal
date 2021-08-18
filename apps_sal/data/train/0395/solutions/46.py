class Solution:

    def populate_jumps(self, sorted_values_idx, jumps):

        stack = []
        for jump_to in sorted_values_idx:

            while(stack and stack[-1] < jump_to):
                jump_from = stack.pop()
                jumps[jump_from] = jump_to

            stack.append(jump_to)

    def oddEvenJumps(self, A: List[int]) -> int:

        odd_jump = [None] * len(A)
        even_jump = [None] * len(A)

        num_idx_array = [(num, idx) for idx, num in enumerate(A)]

        sorted_idxs = list(map(lambda x: x[1], list(sorted(num_idx_array))))

        reverse_sorted_idxs = list(map(lambda x: x[1], list(sorted(num_idx_array, key=lambda x: (-x[0], x[1])))))

        self.populate_jumps(sorted_idxs, odd_jump)
        self.populate_jumps(reverse_sorted_idxs, even_jump)

        odd_dp = [False] * len(A)
        even_dp = [False] * len(A)

        odd_dp[-1] = True
        even_dp[-1] = True

        result = 1
        print(odd_dp, )
        for start_idx in range(len(A) - 2, -1, -1):

            if odd_jump[start_idx] is not None and even_dp[odd_jump[start_idx]] is True:
                odd_dp[start_idx] = True
                result += 1

            if even_jump[start_idx] is not None and odd_dp[even_jump[start_idx]] is True:
                even_dp[start_idx] = True

        return result
