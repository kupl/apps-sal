class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n, target = len(arr), len(arr) // 2
        counts = {}
        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        counts = sorted(list(counts.values()), reverse=True)

        numRemoved = 0
        for i in counts:
            n -= i
            numRemoved += 1
            if n <= target:
                return numRemoved

        return numRemoved
