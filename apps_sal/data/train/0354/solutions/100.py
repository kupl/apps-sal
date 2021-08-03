import collections as clc
import functools as ft


class Solution:

    BASE = 10 ** 9 + 7

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        state = clc.defaultdict(int)
        state[1, 0] = 1
        for _ in range(n):
            new_state = clc.defaultdict(int)
            for (last_roll, streak), count in list(state.items()):
                for dice in range(1, 7):
                    if dice == last_roll:
                        if streak >= rollMax[last_roll - 1]:
                            continue
                        new_state[dice, streak + 1] = (new_state[dice, streak + 1] + count) % self.BASE
                    else:
                        new_state[dice, 1] = (new_state[dice, 1] + count) % self.BASE
            state = new_state
        return sum(state.values()) % self.BASE
