class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        best = [float('inf') for _ in ranges]
        for i, r in enumerate(ranges):
            if r > 0:
                start, end = i - r, i + r
                best_with = 1 + (best[start] if start > 0 else 0)
                for j in range(max(0, start), min(len(ranges), end + 1)):
                    best[j] = min(best[j], best_with)
        if any(v for v in best if v == float('inf')):
            return -1
        return best[-1]
