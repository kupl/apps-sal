class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d = sorted([(difficulty[i],profit[i]) for i in range(len(difficulty))])
        c = [0] * 100005
        
        # print(d)
        
        t = 0
        for i in range(1,100005):
            c[i] = c[i-1]
            while t < len(d) and i == d[t][0]:
                c[i] = max(c[i],d[t][1])
                t += 1
                
        
        # print(c[0:101])
        # print([c[i] for i in worker])
        
        return sum([c[i] for i in worker])
