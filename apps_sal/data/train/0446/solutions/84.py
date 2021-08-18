class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = collections.Counter(arr)
        items = [(k, v) for k, v in list(c.items())]
        items.sort(key=lambda x: x[1])
        removals = 0
        i = 0
        while removals < k and i < len(items):
            ky = items[i][0]
            if c[ky] == 1:
                del c[ky]
                i += 1
            else:
                c[ky] -= 1
            removals += 1
        return len(c)
