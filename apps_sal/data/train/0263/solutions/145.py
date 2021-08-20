class Solution:

    def knightDialer(self, n):
        max_val = 10 ** 9 + 7
        mem = {(1, 1): 1, (1, 2): 1, (1, 3): 1, (1, 4): 1, (1, 5): 1, (1, 6): 1, (1, 7): 1, (1, 8): 1, (1, 9): 1, (1, 0): 1}
        fields = {0: (4, 6), 1: (6, 8), 2: (7, 9), 3: (4, 8), 4: (3, 9, 0), 5: (), 6: (0, 1, 7), 7: (2, 6), 8: (3, 1), 9: (2, 4)}
        new_mem = {}
        for length in range(1, n):
            for num in range(10):
                possible_jumps = fields[num]
                possible_paths = 0
                for jump in possible_jumps:
                    possible_paths = (possible_paths + mem[length, jump]) % max_val
                new_mem[length + 1, num] = possible_paths
            mem = new_mem
            new_mem = {}
        result = 0
        for key in list(mem.keys()):
            result = (result + mem[key]) % max_val
        return result % max_val
