import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        facts=[]
        for i in range(1,n+1):
            if n%i==0:
                facts.append(i)
        if len(facts)<k:
            return -1
        else:
            return facts[k-1]
            

