class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        mem = []
        for di in range(d + 1):
            cr = [0 for i in range(target + 1)]
            mem.append(cr)
        mem[0][0] = 1
        print(mem)
        for ti in range(1, target + 1):
            for di in range(1, d + 1):
                for fi in range(1, f + 1):
                    if ti - fi >= 0:
                        mem[di][ti] += mem[di - 1][ti - fi]
        return mem[d][target] % MOD
