class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = {}
        for element in arr:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1
        counts_sorted = sorted(counts.items(), key=lambda x: x[1], reverse=False)
        while len(counts_sorted) > 0 and k >= counts_sorted[0][1]:
            removed = counts_sorted.pop(0)
            k -= removed[1]
        return len(counts_sorted)
