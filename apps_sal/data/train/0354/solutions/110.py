class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        from collections import defaultdict
        LARGE = int(1e9 + 7)

        die_prev_to_combination = {(i, 1): 1 for i in range(1, 7)}
        for i in range(n - 1):
            next_die_prev_to_combination = defaultdict(int)
            for die_and_prev, combination in list(die_prev_to_combination.items()):
                die, prev = die_and_prev
                for next_die in range(1, 7):
                    if next_die == die:
                        if prev == rollMax[die - 1]:
                            continue
                        else:
                            next_die_prev_to_combination[(next_die, prev + 1)] += combination
                    else:
                        next_die_prev_to_combination[(next_die, 1)] += combination
            die_prev_to_combination = next_die_prev_to_combination

        return sum(c for d, c in list(die_prev_to_combination.items())) % LARGE
