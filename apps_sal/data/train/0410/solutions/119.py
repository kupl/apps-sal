class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        dp_steps = {}

        def find_power(n: int) -> int:
            if n in dp_steps:
                return dp_steps[n]
            elif n == 1:
                return 0
            else:
                if n % 2 == 0:
                    return 1 + find_power(n // 2)
                else:
                    return 1 + find_power(n * 3 + 1)

        results = []
        for i in range(lo, hi + 1):
            results.append((find_power(i), i))
        results.sort()
        return results[k - 1][1]
