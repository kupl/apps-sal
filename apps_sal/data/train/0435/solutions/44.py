from collections import defaultdict

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        seen = defaultdict(int, {0: 1})
        ret = psum = 0
        for n in A:
            psum = (psum + n) % K
            if psum in seen:
                ret += seen[psum]
            seen[psum] += 1
        return ret
