class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        if arrLen>steps//2+1:
            arrLen=steps//2+1
        num_ways=[0 for i in range(arrLen)]
        num_ways[0]=1
        k=10**9+7
        for _ in range(steps):
            cur_num_ways=num_ways[:]
            for i in range(arrLen):
                if i-1>=0:
                    cur_num_ways[i]+=num_ways[i-1]
                if i+1<arrLen:
                    cur_num_ways[i]+=num_ways[i+1]
                cur_num_ways[i]=cur_num_ways[i]%k
            num_ways=cur_num_ways
        return num_ways[0]
                    
                    

