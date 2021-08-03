class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        if n == 1:
            return 6
        mem = {}

        def get_dp(n, d, c):
            if n == 1:
                return 6 if c < rollMax[d - 1] else 5
            elif (n, d, c) not in mem:
                mem[n, d, c] = 0
                for d_ in range(1, 7):
                    if d_ != d:
                        mem[n, d, c] += get_dp(n - 1, d_, 1)
                    elif c < rollMax[d - 1]:
                        mem[n, d, c] += get_dp(n - 1, d, c + 1)
            return mem[n, d, c]
        result = sum(get_dp(n - 1, d, 1) for d in range(1, 7))
        result = result % int(10**9 + 7)
        return result
