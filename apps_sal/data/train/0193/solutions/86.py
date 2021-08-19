class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        targetLen = len(arr) / 2
        elementsRemoved = depth = 0
        data = collections.Counter(arr)
        for (key, val) in data.most_common():
            elementsRemoved += val
            depth += 1
            if elementsRemoved >= targetLen:
                return depth
