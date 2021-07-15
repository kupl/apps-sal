class Solution:
    def minOperationsMaxProfit(self, cus: List[int], p: int, l: int) -> int:
        onboard = 0
        waiting = 0
        ans = -float('inf')
        s=0
        res = 0
        count=0
        for i in range(len(cus)):
            count+=1
            waiting+=cus[i]
            if(waiting>=4):
                onboard+=4
                waiting-=4
                s+=(p*4-l*1)
                
            else:
                onboard+=waiting
                s+= (p*waiting-l*1)
                waiting=0
                
            if(s>ans):
                res = count
                ans =s
            
        if(waiting>0):
            while(waiting!=0):
                count+=1
                if(waiting>=4):
                    waiting-=4
                    s+=(p*4-l*1)

                else:
                    s+= (p*waiting-l*1)
                    waiting=0
                    
                if(s>ans):
                    res = count
                    ans =s

        if(ans<0):
            return -1
        return res
                    
        

            

