def answer(x, y, alice, bob):
    if alice[x] > bob[y]:
        return 'Alice'
    elif alice[x] < bob[y]:
        return 'Bob'
    else:
        return 'Tie'


class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        if len(stoneValue) == 1:
            if stoneValue[0] > 0:
                return 'Alice'
            elif stoneValue[0] == 0:
                return 'Tie'
            else:
                return 'Bob'
        alice = [0] * len(stoneValue)
        bob = [0] * len(stoneValue)
        alice[-1] = stoneValue[-1]
        bob[-1] = stoneValue[-1]
        cumSumm = [0] * len(stoneValue)
        summ = stoneValue[-1]
        cumSumm[-1] = summ
        for i in range(len(stoneValue) - 2, -1, -1):
            summ += stoneValue[i]
            cumSumm[i] = summ
            if i + 2 == len(stoneValue):
                alice[i] = max(stoneValue[i] + stoneValue[i + 1], stoneValue[i] + cumSumm[i + 1] - bob[i + 1])
                bob[i] = max(stoneValue[i] + stoneValue[i + 1], stoneValue[i] + cumSumm[i + 1] - alice[i + 1])
                continue
            if i + 3 == len(stoneValue):
                alice[i] = max(stoneValue[i] + cumSumm[i + 1] - bob[i + 1], stoneValue[i] + stoneValue[i + 1] + cumSumm[i + 2] - bob[i + 2], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2])
                bob[i] = max(stoneValue[i] + cumSumm[i + 1] - alice[i + 1], stoneValue[i] + stoneValue[i + 1] + cumSumm[i + 2] - alice[i + 2], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2])
                continue
            alice[i] = max(stoneValue[i] + cumSumm[i + 1] - bob[i + 1], stoneValue[i] + stoneValue[i + 1] + cumSumm[i + 2] - bob[i + 2], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + cumSumm[i + 3] - bob[i + 3])
            bob[i] = max(stoneValue[i] + cumSumm[i + 1] - alice[i + 1], stoneValue[i] + stoneValue[i + 1] + cumSumm[i + 2] - alice[i + 2], stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + cumSumm[i + 3] - alice[i + 3])
        if len(stoneValue) == 2:
            i = 0
            if alice[0] == stoneValue[i] + cumSumm[i + 1] - bob[i + 1]:
                (x, y) = (i, i + 1)
            return answer(x, y, alice, bob)
        if len(stoneValue) == 3:
            i = 0
            if alice[0] == stoneValue[i] + cumSumm[i + 1] - bob[i + 1]:
                (x, y) = (i, i + 1)
            elif alice[0] == stoneValue[i] + stoneValue[i + 1] + cumSumm[i + 2] - bob[i + 2]:
                (x, y) = (i, i + 2)
            return answer(x, y, alice, bob)
        i = 0
        if alice[0] == stoneValue[i] + cumSumm[i + 1] - bob[i + 1]:
            (x, y) = (i, i + 1)
        elif alice[0] == stoneValue[i] + stoneValue[i + 1] + cumSumm[i + 2] - bob[i + 2]:
            (x, y) = (i, i + 2)
        elif alice[0] == stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] + cumSumm[i + 3] - bob[i + 3]:
            (x, y) = (i, i + 3)
        return answer(x, y, alice, bob)
