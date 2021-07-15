class Solution:
    def minCost(self, S: str, cost: List[int]) -> int:
        def checkStr(s):
            i=1
            out = []
            while i<len(s):
                j=i
                out1 = set([])
                if s[j]==s[j-1]:
                    while j<len(s) and s[j]==s[j-1]:
                        out1.add(j-1)
                        out1.add(j)
                        j+=1
                    out.append(list(out1))
                    i=j
                else:
                    i+=1
            return out
        
        cst = 0
        s = list(S)
        indexes = checkStr(s)
        # print (indexes)
        i=0
        while i<len(indexes):
            curr = indexes[i]
            costs = list(map(lambda x:cost[x], curr))
            # print (costs)
            cst+=sum(costs)-max(costs)
            i+=1
        return cst
