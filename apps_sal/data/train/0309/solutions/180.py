from itertools import repeat
from collections import Counter


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        length = len(A)
        onleft = set()
        onleftl = []
        onright = dict(Counter(A))
        toextend = [{} for _ in range(501)]
        res = 2
        for i in range(0, length):
            val = A[i]
            tex = toextend[val]
            onright[val] -= 1
            for lval in onleftl:
                diff = val - lval
                nextval = val + diff
                if onright.get(nextval, 0) == 0:
                    continue
                c = tex.get(diff, 2) + 1
                if c > res:
                    res = c
                toextend[nextval][diff] = c
            if val not in onleft:
                onleftl.append(val)
                onleft.add(val)
        return res
