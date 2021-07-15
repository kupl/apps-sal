class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        items = sorted(list(counter.items()), key=lambda x: -x[1])
        left = k
        while left > 0 and items:
            if items[-1][1] <= left:
                left -= items[-1][1]
                items.pop()
            else:
                break
        return len(items)


