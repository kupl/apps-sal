class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        
        def findProfit(ppl, goodJobs):
            l=0
            r=len(goodJobs)-1
            while l<r-1:
                test=int((l+r)/2)
                if goodJobs[test][1]>ppl:
                    l=test
                else:
                    r=test
            if goodJobs[r][1]>ppl:
                return 0
            elif goodJobs[l][1]>ppl:
                return goodJobs[r][0]
            return goodJobs[l][0]
                
        
        goodJobs=[]
        jobs=[(profit[i], difficulty[i]) for i in range(len(difficulty))]
        jobs=sorted(jobs, key=lambda job:job[0], reverse=True)
        goodJobs.append(jobs[0])
        for i in range(1,len(jobs)):
            if jobs[i][1]<goodJobs[-1][1]:
                goodJobs.append(jobs[i])
        ans=0
        print((goodJobs, worker))
        for ppl in worker:
            ans=ans+findProfit(ppl, goodJobs)
            print(ans)
        return ans
         

