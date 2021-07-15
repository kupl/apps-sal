class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        counts = defaultdict(int)
        for x in sorted(A):
            counts[x] += 1
            if x < 0 and x * 2 in counts:
                while counts[x] > 0 and counts[x * 2] > 0:
                    counts[x] -= 1
                    counts[x * 2] -= 1
            if x >= 0 and x / 2 in counts:
                while counts[x] > 0 and counts[x / 2] > 0:
                    counts[x] -= 1
                    counts[x / 2] -= 1
        return sum(c for v, c in counts.items()) == 0
