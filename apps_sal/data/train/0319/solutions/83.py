class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        record = {}

        def helper(i):
            if i in record:
                return record[i]
            if i >= len(stoneValue):
                return [0, 0]
            (a, b) = (float('-inf'), float('-inf'))
            for x in range(i, min(i + 3, len(stoneValue))):
                temp = helper(x + 1)
                (tempa, tempb) = (sum(stoneValue[i:x + 1]) + temp[1], temp[0])
                if tempa > a:
                    (a, b) = (tempa, tempb)
            record[i] = [a, b]
            return [a, b]
        (a, b) = helper(0)
        if a > b:
            return 'Alice'
        elif a < b:
            return 'Bob'
        else:
            return 'Tie'
