class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q=initialBoxes
        has_key=[0]*len(status)
        has_open=[0]*len(status)
        res=0
 
        while q:
            qq=[]
            for s in q:
                if status[s] or has_key[s]:
                    res+=candies[s]
                    has_open[s]=1
                    for b in containedBoxes[s]:
                        if has_open[b]: continue
                        qq.append(b)
                    for k in keys[s]:
                        has_key[k]=1
                else:
                    qq.append(s)
            if tuple(qq)==tuple(q): break
            q,qq=qq,[]
 
        return res
