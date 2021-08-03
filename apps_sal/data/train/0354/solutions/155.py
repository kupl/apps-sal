class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def ways(side, already, rolls, mem):
            key = (side, already, rolls)
            if key in mem:
                return mem[key]

            if already >= rollMax[side]:
                mem[key] = 0
                return 0

            if rolls == 0:
                mem[key] = 1
                return 1

            ans = 0
            ans += ways(side, already + 1, rolls - 1, mem)
            for i in range(6):
                if i == side:
                    continue
                ans += ways(i, 0, rolls - 1, mem)

            mem[key] = ans % (10 ** 9 + 7)
            return mem[key]

        ans = 0
        mem = {}
        for i in range(6):
            ans += ways(i, 0, n - 1, mem)
        return ans % (10 ** 9 + 7)
