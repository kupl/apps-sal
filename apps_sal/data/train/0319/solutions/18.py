class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        rowlen = len(stones)
        i = rowlen - 1
        i_1, i_2, i_3 = 0, 0, 0

        while i >= 0:

            answer = -float('inf')

            answer = max(answer, stones[i] - i_1)

            if i + 1 < rowlen:
                answer = max(answer, stones[i] + stones[i + 1] - i_2)

            if i + 2 < rowlen:
                answer = max(answer, stones[i] + stones[i + 1] + stones[i + 2] - i_3)

            i_3 = i_2
            i_2 = i_1
            i_1 = answer
            i -= 1

        if i_1 > 0:
            return 'Alice'
        elif i_1 < 0:
            return 'Bob'
        else:
            return 'Tie'
