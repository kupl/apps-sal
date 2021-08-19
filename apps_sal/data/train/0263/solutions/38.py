class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        transition = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        vec = [1 for _ in range(10)]
        for n in range(1, n):
            new_vec = [0 for _ in range(10)]
            for i in range(0, 10):
                for j in transition[i]:
                    new_vec[j] = (new_vec[j] + vec[i]) % (1000000000 + 7)
            vec = new_vec
        return sum(vec) % (1000000000 + 7)
