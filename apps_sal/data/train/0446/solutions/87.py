class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        bucket = [[] for _ in range(len(arr) + 1)]
        counter = collections.Counter(arr)
        for (key, value) in counter.items():
            bucket[value].append(key)
        for c in range(len(bucket)):
            if k == 0:
                break
            while bucket[c] and k >= c:
                del counter[bucket[c].pop()]
                k -= c
        return len(counter)
