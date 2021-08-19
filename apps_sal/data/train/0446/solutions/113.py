class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = {}
        for item in arr:
            counter[item] = 1 + counter.get(item, 0)
        values = sorted(counter.values())
        removed = 0
        for v in values:
            if v > k:
                break
            else:
                k -= v
                removed += 1
        return len(values) - removed
