class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [],
                 [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        mem = {}
        MOD = 10**9 + 7

        def get(start, k):
            if k == 1:
                return 1
            if (start, k) in mem:
                return mem[start, k]
            total = 0
            for nxt in moves[start]:
                total += get(nxt, k - 1)
                total = total % MOD

            mem[start, k] = total
            return total

        ret = 0
        for x in range(10):
            ret += get(x, n)
            ret = ret % MOD
        return ret
