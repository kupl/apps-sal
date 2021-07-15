class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        if amount==0: return 0
        if amount<min(coins):
            return -1
        
        l = min(coins)
        
        A = [0 for i in range(amount+1)]
        A[l] = 1
        
        for i in range(1,amount+1):
            A[i] = float('inf')
            for coin in coins:
                if i>coin and A[i-coin]>0:
                    A[i] = min(A[i],1+A[i-coin])
                elif i==coin: A[i] = 1
            if A[i]==float('inf'):
                A[i]=0
                           
                           
                
                
        print(A)
        if A[amount]==0: return -1
        return A[amount]
                

