class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        rollMax.insert(0, None)
        memo = {}

        def recurse(curr_n, curr_num, seq_length):
            if (curr_n, curr_num, seq_length) in memo:
                return memo[curr_n, curr_num, seq_length]
            if curr_n == n:
                return 1
            comb = 0
            for i in range(1, len(rollMax)):
                if i == curr_num and rollMax[i] - seq_length > 0:
                    comb += recurse(curr_n + 1, curr_num, seq_length + 1)
                elif i != curr_num:
                    comb += recurse(curr_n + 1, i, 1)
            memo[curr_n, curr_num, seq_length] = comb
            return comb
        combs = 0
        for i in range(1, 7):
            combs += recurse(1, i, 1)
        return combs % 1000000007
