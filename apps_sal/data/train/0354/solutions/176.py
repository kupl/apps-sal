class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mem = {}
        mod = int(10 ** 9) + 7

        def rec(n, li, k):
            if n == 0:
                return 1
            elif (n, li, k) in mem:
                return mem[n, li, k]
            else:
                ans = 0
                for i in range(6):
                    if i == li:
                        if k + 1 <= rollMax[li]:
                            ans += rec(n - 1, li, k + 1) % mod
                    else:
                        ans += rec(n - 1, i, 1) % mod
                mem[n, li, k] = ans % mod
                return ans % mod
        return rec(n, 0, 0) % mod
