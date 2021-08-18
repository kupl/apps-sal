class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        rowlen = len(stones)
        dp = [0] * (rowlen + 1)
        i = rowlen - 1

        while i >= 0:

            answer = -float('inf')

            answer = max(answer, stones[i] - dp[i + 1])

            if i + 1 < rowlen:
                answer = max(answer, stones[i] + stones[i + 1] - dp[i + 2])

            if i + 2 < rowlen:
                answer = max(answer, stones[i] + stones[i + 1] + stones[i + 2] - dp[i + 3])

            dp[i] = answer
            i -= 1

        print(dp)
        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'

        '''
        rowlen=len(stones)
        index=0
        memo=[-1] * rowlen
             
        def helper(index,memo):
            
            if index >= rowlen:
                return 0
            elif memo[index] != -1:
                return memo[index] 
            else:
                answer=-float('inf')
                answer=max(answer,stones[index] - helper(index+1,memo))
                if index + 1 < rowlen:
                    answer=max(answer,stones[index]+stones[index+1] - helper(index+2,memo))
                
                if index + 2 < rowlen:
                    answer=max(answer,stones[index]+stones[index+1]+stones[index+2] - helper(index+3,memo))
                
                memo[index]=answer
                return memo[index]      
                
        answer=helper(0,memo)
        print(answer)
        
        if answer < 0:
            return 'Bob'
        elif answer > 0:
            return 'Alice'
        else:
            return 'Tie'
            
        '''
