import itertools
from collections import Counter
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        ref = [ [letter,len(list(s))] for letter,s in itertools.groupby(text)]
        count = Counter(text)
        res = max( [ min(count.get(i), k + 1) for i , k in ref] ) 
        for i in range(1,len(ref) - 1):
            if ref[i-1][0] == ref[i+1][0] and ref[i][1] == 1 : 
                res = max(res, min(ref[i-1][1] + ref[i+1][1] + 1, count.get(ref[i-1][0]))  )
        return res
