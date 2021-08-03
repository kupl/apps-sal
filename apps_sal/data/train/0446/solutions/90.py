class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        for i, value in sorted(list(counter.items()), key=lambda x: x[1]):
            val = k
            k -= value
            counter[i] -= val
            if counter[i] <= 0:
                del counter[i]
        return len(counter)
