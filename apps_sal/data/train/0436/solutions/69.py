class Solution:
    def minDays(self, n: int) -> int:
        q=[n]
        seen = set()
        res=0
        while q:
            nq=[]
            for x in q: # SIMPLE BFS
                if x==0: 
                    return res
                cur=x
                seen.add(cur)
                if cur%2==0 and cur/2 not in seen:
                    nq.append(cur/2)
                if cur%3==0 and cur/3 not in seen:
                    nq.append(cur/3)
                if cur-1 not in seen:
                    nq.append(cur-1)
            q=nq
            res+=1

