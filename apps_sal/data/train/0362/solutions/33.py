class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        total = 1 << len(hats)
        (satisfy, bound) = ([0] * 41, 0)
        for (i, likes) in enumerate(hats):
            for hat in likes:
                satisfy[hat] |= 1 << i
                bound = max(bound, hat)
        MOD = 10 ** 9 + 7
        DP = [1] + [0] * (total - 1)
        for hat in range(1, bound + 1):
            new_DP = [0] * total
            for state in range(total):
                new_DP[state] = DP[state]
                (can_satisfy, mask) = (satisfy[hat] & state, 1)
                while can_satisfy != 0:
                    if can_satisfy & 1:
                        new_DP[state] += DP[state ^ mask]
                    can_satisfy >>= 1
                    mask <<= 1
                new_DP[state] %= MOD
            DP = new_DP
        return DP[total - 1]
