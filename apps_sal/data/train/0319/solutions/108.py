class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        firstSelect = True  # True denoted Alice select first, False for Bob
        initIndex = 0
        stoneValueLength = len(stoneValue)
        mem = {}

        if stoneValueLength == 0:
            return 'Tie'
        else:
            result = self.recursiveHelper(stoneValue, stoneValueLength, initIndex, firstSelect, mem)
            # print(result)
            if result > 0:
                return 'Alice'
            elif result < 0:
                return 'Bob'
            else:
                return 'Tie'

    def recursiveHelper(self, stoneValue: List[int], length: int, index: int, flag: bool, mem: dict) -> int:

        if index >= length:
            return 0

        memV = mem.get((index, flag))
        if memV is not None:
            return memV

        minus = length - index
        if minus == 1:  # only one choice
            curr = stoneValue[index]
            c1 = curr if flag else -curr
            mem[(index, flag)] = c1
            return c1
        elif minus == 2:  # two choices
            # 1 select all two
            curr = stoneValue[index] + stoneValue[index + 1]
            c1 = curr if flag else -curr

            # 2 select the first one
            curr = stoneValue[index]
            c2 = (curr if flag else -curr) + self.recursiveHelper(stoneValue, length, index + 1, not flag, mem)

            result = max(c1, c2) if flag else min(c1, c2)
            mem[(index, flag)] = result
            return result
        else:  # >= 3; three choices
            # 1 select all three
            curr = stoneValue[index] + stoneValue[index + 1] + stoneValue[index + 2]
            c1 = (curr if flag else -curr) + self.recursiveHelper(stoneValue, length, index + 3, not flag, mem)

            # 2 select the first two
            curr = stoneValue[index] + stoneValue[index + 1]
            c2 = (curr if flag else -curr) + self.recursiveHelper(stoneValue, length, index + 2, not flag, mem)

            # 3 select the first one
            curr = stoneValue[index]
            c3 = (curr if flag else -curr) + self.recursiveHelper(stoneValue, length, index + 1, not flag, mem)
            result = max(c1, c2, c3) if flag else min(c1, c2, c3)
            mem[(index, flag)] = result
            return result
