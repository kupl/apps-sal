class Solution:

    def stoneGameIII(self, stones: List[int]) -> str:
        rowlen = len(stones)
        i = rowlen - 1
        (i_1, i_2, i_3) = (0, 0, 0)
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
        "\n        # Recursion + TopDown\n        rowlen=len(stones)\n        index=0\n        memo=[-1] * rowlen\n             \n        def helper(index,memo):\n            \n            if index >= rowlen:\n                return 0\n            elif memo[index] != -1:\n                return memo[index] \n            else:\n                answer=-float('inf')\n                answer=max(answer,stones[index] - helper(index+1,memo))\n                if index + 1 < rowlen:\n                    answer=max(answer,stones[index]+stones[index+1] - helper(index+2,memo))\n                \n                if index + 2 < rowlen:\n                    answer=max(answer,stones[index]+stones[index+1]+stones[index+2] - helper(index+3,memo))\n                \n                memo[index]=answer\n                return memo[index]      \n                \n        answer=helper(0,memo)\n        print(answer)\n        \n        if answer < 0:\n            return 'Bob'\n        elif answer > 0:\n            return 'Alice'\n        else:\n            return 'Tie'\n            \n        "
