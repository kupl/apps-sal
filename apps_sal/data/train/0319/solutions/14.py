class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # aliceScore = [0]
        # bobScore = [0]
        # INVALID = 's'
        # def helper(stoneValues,index,aliceScore,bobScore,aliceTurn):
        #     scoreToUpdate = aliceScore
        #     if not aliceTurn:
        #         scoreToUpdate = bobScore
        #     if len(stoneValues) - 1 == index:
        #         scoreToUpdate[0] += stoneValues[index]
        #         return
        #     bck = scoreToUpdate[0]
        #     sums = []
        #     for i in range(1,4):
        #         scoreToUpdate[0] = bck
        #         if i + index <= len(stoneValues):
        #             for j in range(i):
        #                 scoreToUpdate[0] += stoneValues[index+j]
        #             helper(stoneValues,index + i,aliceScore,bobScore,not aliceTurn)
        #             sums.append(scoreToUpdate[0])
        #     if len(sums) > 0:
        #         scoreToUpdate[0] = max(sums)
        #     else:
        #         scoreToUpdate[0] = bck
        #     return
        # helper(stoneValue,0,aliceScore,bobScore,True)
        # if aliceScore[0] > bobScore[0]:
        #     return 'Alice'
        # elif bobScore[0] > aliceScore[0]:
        #     return 'Bob'
        # return 'Tie'
        mem = {}

        def helper(stoneValues, index):
            if index in mem:
                return mem[index]
            if index >= len(stoneValues):
                return 0
            ans = stoneValues[index] - helper(stoneValues, index + 1)
            if index + 1 < len(stoneValues):
                temp = stoneValues[index] + stoneValues[index + 1] - helper(stoneValues, index + 2)
                ans = max(ans, temp)
            if index + 2 < len(stoneValues):
                temp = stoneValues[index] + stoneValues[index + 1] + stoneValues[index + 2] - helper(stoneValues, index + 3)
                ans = max(ans, temp)
            mem[index] = ans
            return ans
        ans = helper(stoneValue, 0)
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        return 'Tie'
