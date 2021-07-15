class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        bfb = [0]*max(max(worker),max(difficulty)) # bfb[i] will tell us the best profitting job that is at or below difficulty i+1
        for diff,prof in sorted(zip(difficulty,profit)):
            bfb[diff-1] = max(bfb[diff-1],prof)
        
        currMax = 0
        for i in range(len(bfb)):
            bfb[i] = max(currMax,bfb[i])
            currMax = bfb[i]
            
        # print(bfb)
        
        total = 0
        for w in worker:
            total += bfb[w-1]
            
        return total
