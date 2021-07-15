class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort(key=lambda x:x[1], reverse=True)
        jobs.sort(key=lambda x:x[0])
        bestjobs=[]
        res = 0
        for a,b in jobs:
            if not bestjobs:
                bestjobs.append((a,b))
            elif bestjobs[-1][1]<b:
                bestjobs.append((a,b))
        print(bestjobs)
        for wo in worker:
            lo, hi = 0, len(bestjobs)-1
            while lo<hi:
                mid = (lo+hi+1)//2
                if bestjobs[mid][0]>wo:
                    hi = mid-1
                else:
                    lo = mid
            if bestjobs[lo][0]<=wo:
                res+=bestjobs[lo][1]
        return res

