class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:

        rowlen = len(stones)
        index = 0
        memo = [-1] * rowlen

        def helper(index, memo):

            if index >= rowlen:
                return 0
            elif memo[index] != -1:
                return memo[index]
            else:
                answer = -float('inf')
                answer = max(answer, stones[index] - helper(index + 1, memo))
                if index + 1 < rowlen:
                    answer = max(answer, stones[index] + stones[index + 1] - helper(index + 2, memo))

                if index + 2 < rowlen:
                    answer = max(answer, stones[index] + stones[index + 1] + stones[index + 2] - helper(index + 3, memo))

                memo[index] = answer
                return memo[index]

        answer = helper(0, memo)
        print(answer)

        if answer < 0:
            return 'Bob'
        elif answer > 0:
            return 'Alice'
        else:
            return 'Tie'
