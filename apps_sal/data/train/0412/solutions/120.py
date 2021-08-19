class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        arr = [[0 for i in range(target + 1)] for i in range(d)]

        for i in range(1, min(f, target) + 1):
            arr[0][i] = 1

        for row in range(1, d):
            temp = 0
            for col in range(row + 1, target + 1):
                temp += arr[row - 1][col - 1]
                if col >= f + 1:
                    temp -= arr[row - 1][col - f - 1]

                arr[row][col] = temp

        # for i in range(len(arr)):
        #     print(i, arr[i])

        return arr[d - 1][target] % (1000000007)
