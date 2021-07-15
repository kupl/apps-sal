class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        best = {}; S =0; N = len(stoneValue)
        cumsum = [0 for val in stoneValue]+[0];
        for ii in range(len(stoneValue)-1,-1,-1):
            S = S+stoneValue[ii]
            cumsum[ii] = S
        def findbest(index,stoneValue):
#            print(index,best)
            if index in best:
                res = best[index]
            elif index==len(stoneValue)-1:
                res= stoneValue[-1]
            elif index>=len(stoneValue):
                res = 0  
            else:
                res = -10000000
                for j in range(index+1,min(index+4,N+1)):
                    res = max(res,sum(stoneValue[index:j]) + cumsum[j]-findbest(j,stoneValue))
#                    print(index,j,res)
            best[index] = res
            return best[index]
        res= findbest(0,stoneValue)
#        print(best)
        if res>sum(stoneValue)/2:
            return 'Alice'
        elif res<sum(stoneValue)/2:
            return 'Bob'
        else:
            return 'Tie'
