from collections import defaultdict
from operator import add


def accum(op, l):
    if not l:
        return []
    v = l[0]
    ret = [v]
    for x in l[1:]:
        v = op(v, x)
        ret.append(v)
    return ret


class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        B = accum(add, A)
        B = [0] + B
        B = [x % K for x in B]
        seen = defaultdict(lambda: 0)
        seen[0] = 1
        combinations = 0
        for s in B[1:]:
            target = s
            if seen[target] > 0:
                combinations += seen[target]
            seen[s] = seen[s] + 1
        return combinations
