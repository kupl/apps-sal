class Solution:

    def stoneGameIII(self, stoneValue: list) -> str:

        def play(preSum, index, cache):
            if index == len(preSum) - 1:
                return preSum[index]
            if index in cache:
                return cache[index]
            res = -2 ** 31
            for i in range(1, 4):
                if index + i >= len(preSum):
                    break
                take = preSum[index] - preSum[index + i]
                res = max(res, take + preSum[index + i] - play(preSum, index + i, cache))
            cache[index] = res
            return res
        for i in range(len(stoneValue) - 2, -1, -1):
            stoneValue[i] += stoneValue[i + 1]
        aliceScore = play(stoneValue + [0], 0, {})
        bobScore = stoneValue[0] - aliceScore
        if bobScore > aliceScore:
            return 'Bob'
        elif aliceScore > bobScore:
            return 'Alice'
        else:
            return 'Tie'
