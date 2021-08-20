class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        table = [[0 for i in range(n + 1)] for j in range(7)]

        def helper(n: int, rollMax: List[int], last: int) -> int:
            if n == 0:
                return 1
            if table[last][n] > 0:
                return table[last][n]
            total = 0
            for i in range(1, 7):
                if i == last:
                    continue
                for j in range(1, rollMax[i - 1] + 1):
                    if j > n:
                        break
                    total += helper(n - j, rollMax, i)
            table[last][n] = total % 1000000007
            return total % 1000000007
        ans = helper(n, rollMax, -1)
        print(table)
        return table[-1][-1]
