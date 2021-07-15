from collections import defaultdict

def getPower(i):
    if i==1:
        return 0
    if i%2==0:
        return getPower(i/2) + 1
    else:
        return getPower(i*3+1) + 1

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d=defaultdict(int)
        for i in range(lo, hi+1):
            d[i]=getPower(i)
        sd={k: v for k, v in sorted(list(d.items()), key=lambda item: item[1])}
        
        return list(sd)[k-1]

