class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        n=len(quality)
        workers=sorted([w/q,q] for q,w in zip(quality,wage))
        que=[]
        res=math.inf
        curQuality=0
        for ratio,q in workers:
            heapq.heappush(que,-q)
            curQuality+=q
            if len(que)>K:
                q2=-heapq.heappop(que)
                curQuality-=q2
            if len(que)==K:
                res=min(res,curQuality*ratio)
        return res
