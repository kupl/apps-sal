class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def helper(currentIndex, n, rollMax, pre, d):
            if currentIndex == n:
                return 1
            elif currentIndex > n:
                return 0
            count = 0
            if (currentIndex, pre) in d:
                return d[currentIndex, pre]
            for index in range(6):
                if index != pre:
                    for repeat in range(1, rollMax[index] + 1):
                        count += helper(currentIndex + repeat, n, rollMax, index, d)
            d[currentIndex, pre] = count
            return count
        rolledCount = [0] * 6
        MOD = 10 ** 9 + 7
        d = {}
        return helper(0, n, rollMax, -1, d) % MOD
