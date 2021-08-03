class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort()
        d = collections.defaultdict(int)
        for a in A:
            if d[2 * a] > 0:
                d[2 * a] -= 1
            elif d[a / 2] > 0:
                d[a / 2] -= 1
            else:
                d[a] += 1
        return not any(d.values())
