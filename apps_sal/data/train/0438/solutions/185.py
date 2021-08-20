from collections import defaultdict


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        bits = [0] * n
        groups = defaultdict(int)
        corner = defaultdict(int)
        result = -1
        for (step, i) in enumerate(arr):
            i = i - 1
            bits[i] = 1
            group = 1
            j = i - 1
            group += corner[j]
            groups[corner[j]] -= 1
            j = i + 1
            group += corner[j]
            groups[corner[j]] -= 1
            groups[group] += 1
            corner[i - corner[i - 1]] = group
            corner[i + corner[i + 1]] = group
            if groups[m]:
                result = step
        return result + 1 if result >= 0 else -1
