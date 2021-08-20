class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        counts = {}
        for (i, elem) in enumerate(arr):
            counts[elem] = 1 if elem not in counts else counts[elem] + 1
        size = len(arr)
        count = 0
        vals = sorted(counts.values(), reverse=True)
        while size > len(arr) / 2:
            maxElem = vals[count]
            size -= maxElem
            count += 1
        return count
