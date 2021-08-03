class Solution:
    seen = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        results = {}
        results[1] = {}
        for i in range(1, min(f, target) + 1):
            results[1][i] = 1
        for i in range(2, d + 1):
            results[i] = {}
            for val, times in list(results[i - 1].items()):
                for j in range(1, min(f, target) + 1):
                    results[i][j + val] = results[i].get(j + val, 0) + times

        return results[d].get(target, 0) % 1000000007
