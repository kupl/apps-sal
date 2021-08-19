class Solution:

    def knightDialer(self, N: int) -> int:
        solution = 0
        self.valid_jumps = {1: [6, 8], 2: [9, 7], 3: [8, 4], 4: [9, 3, 0], 5: [], 6: [7, 1, 0], 7: [2, 6], 8: [1, 3], 9: [4, 2], 0: [4, 6]}
        self.N = N
        self.cache = {}
        solution = 0
        for i in range(10):
            solution += self.jump_around(1, i)
        return solution % (pow(10, 9) + 7)

    def jump_around(self, number_len_so_far, last_number):
        if (number_len_so_far, last_number) in self.cache:
            return self.cache[number_len_so_far, last_number]
        if number_len_so_far == self.N:
            return 1
        else:
            solution_for_this_set = 0
            possible_jumps = self.valid_jumps[last_number]
            for possible_jump in possible_jumps:
                solution_for_this_set += self.jump_around(number_len_so_far + 1, possible_jump)
            self.cache[number_len_so_far, last_number] = solution_for_this_set
            return solution_for_this_set
