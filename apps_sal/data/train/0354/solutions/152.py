class Solution:
    def dieSimulator(self, n: int, roll_max: List[int]) -> int:

        dices = defaultdict(int, {(-1, 0): 1})  # previous n, # of consecutive : ways
        for _ in range(n):

            prev_dices = tuple(dices.items())
            dices.clear()

            for pc, ways in prev_dices:
                prev, consecutive = pc
                for r, r_max in enumerate(roll_max):
                    c = int(r == prev) * consecutive + 1
                    if c <= r_max:
                        dices[r, c] += ways

        return sum(dices.values()) % (10 ** 9 + 7)
