class CountClass:
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency

    def __lt__(self, other):
        return self.frequency < other.frequency

    def getValue(self):
        return self.value

    def getFrequency(self):
        return self.frequency


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        if not arr:
            return 0

        import heapq

        # This map will keep track of the counts
        records = {}
        # Initiate the min-heap
        q = []

        # Saving the counts
        for i in arr:
            if i not in list(records.keys()):
                records[i] = 0
            records[i] += 1

        for key, value in list(records.items()):
            heapq.heappush(q, CountClass(key, value))

        while k != 0 and q:
            node = heapq.heappop(q)
            key = node.getValue()
            val = node.getFrequency()
            if val == 1:
                del records[key]
            else:
                val -= 1
                heapq.heappush(q, CountClass(key, val))
            k -= 1

        return len(records)
