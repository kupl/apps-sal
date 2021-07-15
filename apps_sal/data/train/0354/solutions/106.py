import functools

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        max_remaining = sum(rollMax)

        @functools.lru_cache(None)
        def count_sequences(last_index, last_remaining, rolls_left):
            if last_remaining < 0:
                return 0
            if rolls_left == 0:
                return 1

            sequences_from_here = 0
            for i in range(len(rollMax)):
                if i == last_index:
                    sequences_from_here += count_sequences(i, last_remaining - 1, rolls_left - 1)
                else:
                    sequences_from_here += count_sequences(i, rollMax[i] - 1, rolls_left - 1)
            return sequences_from_here % (10 ** 9 + 7)

        return sum(count_sequences(i, rollMax[i] - 1, n - 1) for i in range(len(rollMax))) % (10 ** 9 + 7)

