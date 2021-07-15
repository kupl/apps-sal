class Solution:
    def dieSimulator(self, n: int, roll_max: List[int]) -> int:
        @lru_cache(maxsize=None)
        def die_simulator(n, consec_num, consec_count):
            if n == 0:
                return 1
            else:
                res = 0
                for i in range(6):
                    if i == consec_num:
                        if roll_max[i] > consec_count:
                            res += die_simulator(n - 1, i, consec_count + 1)
                    elif roll_max[i] != 0:
                        res += die_simulator(n - 1, i, 1)
                return res
                
        return die_simulator(n, -1, 0) % (10 ** 9 + 7)
