class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # get counts of each element
        counts = {}
        for i, elem in enumerate(arr):
            counts[elem] = 1 if elem not in counts else counts[elem]+1
        # keep getting max and checking if the length is less than half upon removal until it is
        size = len(arr)
        count = 0
        vals = sorted(counts.values(),reverse=True)
        while size > len(arr)/2:
            maxElem = vals[count]
            size -= maxElem
            count += 1
        return count
