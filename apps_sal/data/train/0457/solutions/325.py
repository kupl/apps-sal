class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N=[0 for i in range(amount+1)]
        N[0]=0
        for i in range(1,amount+1):
            temp=[i-j for j in coins]
            history=[N[temp2] for temp2 in temp if temp2 <=i and temp2>=0 and N[temp2]!=-1]
            if len(history)==0:
                N[i]=-1
            else:
                N[i]=1+min([N[temp2] for temp2 in temp if temp2 <=i and temp2>=0 and N[temp2]!=-1])
        return N[amount]
                
            
            

