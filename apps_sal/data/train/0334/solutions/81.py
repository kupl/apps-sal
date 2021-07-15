from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        s = list(s)
        idx = [i for i in range(len(s))]
        dic = dict(zip(idx, cost))
        w = 0
        cost = 0
        for k in range(len(s)-1, 0, -1):
            w = k - 1    
            if s[k] == s[w]:
                kCost = dic[k]
                wCost = dic[w]
                if kCost <= wCost:
                    cost += kCost
                    del s[k]
                else:
                    cost += wCost
                    del s[w]
                    dic[w] = dic[k]
        s = ''.join(s)
        return cost
